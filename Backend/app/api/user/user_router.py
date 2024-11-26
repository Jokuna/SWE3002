from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
import uuid

from app.db import get_db
from .user_schema import *
from app.services.session import sessions

def transform_object_id(data):
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

# 로그인
@router.post("/login")
async def login(_user: LoginUser, response: Response, db: AsyncIOMotorDatabase=Depends(get_db)):
    user = await db["User"].find_one({"email": _user.email, "passkey": _user.passkey})

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or passkey")

    session_id = str(uuid.uuid4())
    sessions[session_id] = transform_object_id(user)

    # 세션 쿠키 설정
    response.set_cookie(key="session_id", value=session_id, httponly=True)

    return {"message": "Login successful", "user": transform_object_id(user)}

# 로그아웃
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
    print(_user)
    
    return "register"

# 인증코드 생성 후, 이메일 전송
# 회원가입, 로그인 둘다 사용
@router.post("/genToken")
async def genToken(db: AsyncIOMotorDatabase=Depends(get_db)):
    return "token"

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
async def modify_user_info(_user: ModifyUserInfo, db: AsyncIOMotorDatabase=Depends(get_db)):
    print(_user)
    
    return "modify_user_info"

# 프로필 변경 - 이름
@router.post("/profile/name")
async def modify_user_info_name(db: AsyncIOMotorDatabase=Depends(get_db)):
    return "modify_user_info_name"
