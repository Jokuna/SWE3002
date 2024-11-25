from typing import List

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

from app.db import get_db
from .user_schema import *

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
async def login(_user: LoginUser, db: AsyncIOMotorDatabase=Depends(get_db)):
    return "login"

# 로그아웃
@router.post("/logout")
async def logout(db: AsyncIOMotorDatabase=Depends(get_db)):
    return "logout"

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
