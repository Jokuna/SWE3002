from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List

from app.db import get_db
from app.api.user.user_schema import *
from app.models import *
from app.api.user.jwt import SECRET_KEY, ALGORITHM

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

@router.get("/")
async def hello():
    return "Hello World"


# 검색 옵션 설정 - Basic
@router.post("/filter/basic")
async def set_filter_basic(db: AsyncIOMotorDatabase=Depends(get_db)):
    
    return "filter 설정"

class SleepTimeFilter(BaseModel):
    sleep_time: time
    wake_time: time

# 검색 옵션 설정 - Sleep Time
@router.post("/filter/sleep")
async def set_filter_sleep(sleep_filter: SleepTimeFilter, db: AsyncIOMotorDatabase=Depends(get_db)):
    return "filter 설정"

# 검색 옵션 설정 - Sleep Time
@router.post("/filter/extra")
async def set_filter_extra(db: AsyncIOMotorDatabase=Depends(get_db)):
    return "filter 설정"


# 검색 조회 - 해당 필터값을 기반으로 조회
@router.get("/filter")
async def get_users_by_filter(db: AsyncIOMotorDatabase=Depends(get_db)):
    return ""



