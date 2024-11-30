from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import BaseModel, field_validator, EmailStr
from app.db import get_db
from typing import List

'''
검색 관련 API
1. 검색 필터링 입력
2. 검색
3. 검색 결과 정렬
'''
router = APIRouter(
    prefix="/backend/search",
    tags=["search"]
)

class RegisterUser(BaseModel):
    user_id:            str
    isMale:             bool
    dormitory:          int
    latestGPA:          float
    isSmoke:            bool
    sleepingTime:       str
    wakeTime:           str
    age:                int
    semester:           int
    major:              str
    selfIntroduction:   str
    trait:              list[str]
    weekendProportion:  int
    isOpenAge:          bool
    isOpenMajor:        bool

    

# 검색 조회 - 해당 필터값을 기반으로 조회
@router.post("/filter")
async def post_users_by_filter(_user: RegisterUser, db: AsyncIOMotorDatabase=Depends(get_db)):

    print(_user)
    # 세션에 해당 데이터가 저장될 예정

    return _user.user_id



