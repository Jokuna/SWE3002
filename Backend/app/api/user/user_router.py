import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
import uuid

from app.db import get_db
from app.api.user.user_crud import create_passkey, send_passkey_email
from app.api.user.user_schema import *
from app.services.session import sessions

def transform_object_id(data: dict):
    if data and "_id" in data:
        data["_id"] = str(data["_id"])
    return data

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

# 로그인 & signup 시 인증 검증용으로도 가능?
@router.post("/login")
async def login(_user: LoginUser, response: Response, db: AsyncIOMotorDatabase=Depends(get_db)):
    user: dict = await db["users"].find_one({"email": _user.email})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")
    elif _user.passkey != user["passkey"]:
        raise HTTPException(status_code=401, detail="Invalid passkey")

    session_id = str(uuid.uuid4())
    sessions[session_id] = transform_object_id(user)

    # 세션 쿠키 설정
    response.set_cookie(key="session_id", value=session_id, httponly=True)

    return {"message": "Login successful", "user": transform_object_id(user)}

# 로그아웃 (클라이언트에서 발급한 토큰을 삭제하는 형식으로 구현?)
@router.post("/logout")
async def logout(response: Response, db: AsyncIOMotorDatabase=Depends(get_db)):
    session_id = response.cookies.get("session_id")
    
    if session_id and session_id in sessions:
        del sessions[session_id]  # 세션 삭제
    
    response.delete_cookie("session_id")
    return {"message": "Logged out successfully"}

# 회원가입
@router.post("/register")
async def register(_user: RegisterUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["users"]
    
    # Check if user already exists    
    existing_user = await collection.find_one({"email": _user.email})
    if not existing_user:
        return {"message": "User does not exist"}, 404
    
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
    return {"message": "User updated successfully"}
    

# 인증코드 생성 후, 이메일 전송
# 회원가입, 로그인 둘다 사용
@router.post("/genToken")
async def genToken(_user: GenTokenUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    # Create a passkey
    passkey = create_passkey()
    sent_time = send_passkey_email(_user.email, passkey)
    
    collection = db["users"]
    
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
        
    return {"message": "Successfully send passkey"}

# 현재 로그인 상태 확인
@router.get("/me")
async def get_current_user(request: Request, db: AsyncIOMotorDatabase=Depends(get_db)):
    session_id = request.cookies.get("session_id")
    
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    return {"user": sessions[session_id]}


# 현재 로그인 상태 확인
@router.get("/me")
async def get_current_user(request: Request, db: AsyncIOMotorDatabase=Depends(get_db)):
    session_id = request.cookies.get("session_id")
    
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    return {"user": sessions[session_id]}


# 탈퇴 .. 구현 X

'''
프로필 API
'''
# 프로필 조회
@router.get("/profile/{user_id}")
async def get_user_info(user_id: str, db: AsyncIOMotorDatabase=Depends(get_db)):
    collection = db["users"]
    _user = await collection.find_one({"_id": ObjectId(user_id)})
    _user["_id"] = user_id # ObjectId type can not be iterable
    
    return _user

# 프로필 변경
@router.post("/profile")
async def modify_user_info(request: Request, _user: ModifyUserInfo, db: AsyncIOMotorDatabase=Depends(get_db)):
    session_id = request.cookies.get("session_id")
    
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    collection = db["users"]
    
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
    
    result = await collection.update_one({"_id": ObjectId(session_id)}, {"$set": update_fields})
    return {"message": "UserInfo updated successfully"}

# 프로필 변경 - 이름
@router.post("/profile/name")
async def modify_user_info_name(request: Request, _user: ModifyUserInfoName, db: AsyncIOMotorDatabase=Depends(get_db)):
    session_id = request.cookies.get("session_id")
    
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    collection = db["users"]
    
    # Update the user's name based on user_id
    result = await collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {"username": _user.username}}
    )
    
    if result.modified_count == 1:
        return {"message": "User name updated successfully"}
    else:
        return {"message": "User not found or name not modified"}
