import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from jose import jwt

from app.db import get_db
from app.api.user.user_schema import *
from app.api.user.user_crud import create_passkey, send_passkey_email
from app.api.user.jwt import SECRET_KEY, ALGORITHM

'''
계정 관리 API
'''

router = APIRouter(
    prefix="/backend/user",
    tags=["user"]
)
    
@router.get("/")
async def hello():
    return "Hello World"

'''
인증 API
'''

# 로그인 & signup 시 인증 검증
@router.post("/login")
async def login(_user: LoginUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["User"]
    user: dict = await collection.find_one({"email": _user.email})

    if not user or user["passkey"] != _user.passkey:
        raise HTTPException(status_code=401, detail="Invalid email or passkey")

    # JWT 토큰 발행
    token = jwt.encode({
        "sub": str(user["_id"]), 
        "exp": datetime.now() + timedelta(hours=24)}, 
        SECRET_KEY, algorithm=ALGORITHM)
    
    return {"msg": "Login successful", "token": token}

# 로그아웃 (클라이언트에서 발급한 토큰을 삭제하는 형식으로 구현?)
# JWT 방식이므로, 구현 X
@router.post("/logout")
async def logout(db: AsyncIOMotorDatabase=Depends(get_db)):
    return "logout"

# 회원가입
# 이메일, passkey 검증 후 회원가입
@router.post("/register")
async def register(_user: RegisterUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["User"]
    
    # Check if user already exists    
    existing_user = await collection.find_one({"email": _user.email, "passkey": _user.passkey})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    update_fields = {
        "username": _user.username,
        "userInfo": {
            "isMale": _user.isMale,
            "dormitory": _user.dormitory,
            "latestGPA": _user.latestGPA,
            "isSmoke": _user.isSmoke,
            "sleepingTime": _user.sleepingTime,
            "wakeTime": _user.wakeTime,
            "age": _user.age,
            "semester": _user.semester,
            "major": _user.major,
            "selfIntroduction": _user.selfIntroduction,
            "trait": _user.trait,
            "weekendProportion": _user.weekendProportion
        },
        "userSettings": {
            "isOpenAge": _user.isOpenAge,
            "isOpenMajor": _user.isOpenMajor,
            "isBasicInfoEntered": True
        }
    }
    result = await collection.update_one({"email": _user.email}, {"$set": update_fields})
    return {"msg": "User updated successfully"}
    

# 인증코드 생성 후, 이메일 전송
# 회원가입, 로그인 둘다 사용
@router.post("/genToken")
async def genToken(_user: GenTokenUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    # Create a passkey
    passkey = create_passkey()
    sent_time = send_passkey_email(_user.email, passkey)
    
    collection = db["User"]
    
    # Check if user exists first
    user = await collection.find_one({"email": _user.email})
    if not user:
        # If user doesn't exist, create new user
        await collection.insert_one({
            "email": _user.email,
            "passkey": passkey,
            "passkeySentTime": sent_time
        })
    else:
        # Update existing user
        await collection.update_one(
            {"email": _user.email},
            {"$set": {"passkey": passkey, "passkeySentTime": sent_time}}
        )
        
    return {"msg": "Successfully send passkey"}

# 탈퇴 .. 구현 X

'''
프로필 API
'''

def transform_object_id(data: dict):
    if data and "_id" in data:
        data["_id"] = str(data["_id"])
    return data

@router.get("/profile/info/{user_id}")
async def get_user_info_detail(user_id: str, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["User"]
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user id")

    data = await db["UserInfo"].find_one({"userId": user_id})
    
    return transform_object_id(data)


# 프로필 조회
@router.get("/profile/{user_id}")
async def get_user_info(user_id: str, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["User"]
    user: dict = await collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user id")
    
    user["_id"] = user_id # ObjectId type can not be iterable
    del user["passkey"] # passkey는 frontend로 전달하지 않는다.
    
    return user


# 프로필 변경
@router.post("/profile")
async def modify_user_info(_user: ModifyUserInfo, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["User"]
    
    update_fields = {
        "username": _user.username,
        "userInfo": {
            "isMale": _user.isMale,
            "dormitory": _user.dormitory,
            "latestGPA": _user.latestGPA,
            "isSmoke": _user.isSmoke,
            "sleepingTime": _user.sleepingTime,
            "wakeTime": _user.wakeTime,
            "age": _user.age,
            "semester": _user.semester,
            "major": _user.major,
            "selfIntroduction": _user.selfIntroduction,
            "trait": _user.trait,
            "weekendProportion": _user.weekendProportion
        },
        "userSettings": {
            "isOpenAge": _user.isOpenAge,
            "isOpenMajor": _user.isOpenMajor,
            "isBasicInfoEntered": True
        }
    }
    
    result = await collection.update_one({"_id": ObjectId(_user.token["sub"])}, {"$set": update_fields})
    return {"msg": "UserInfo updated successfully"}

# 프로필 변경 - 이름
@router.post("/profile/name")
async def modify_user_info_name(_user: ModifyUserInfoName, db: AsyncIOMotorDatabase=Depends(get_db)):
    
    collection = db["User"]
    
    # Update the user's name based on user_id
    result = await collection.update_one(
        {"_id": ObjectId(_user.token["sub"])},
        {"$set": {"username": _user.username}}
    )
    print(result.modified_count)
    
    if result.modified_count == 1:
        return {"msg": "User name updated successfully"}
    else:
        raise HTTPException(401, "User not found or name not modified")
