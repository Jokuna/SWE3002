from fastapi import APIRouter, Depends
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

@router.get("/")
async def hello():
    return "Hello World"


# 검색 옵션 설정 - Basic
@router.post("/filter/basic")
async def set_filter_basic():
    return "filter 설정"


# 검색 옵션 설정 - Sleep Time
@router.post("/filter/sleep")
async def set_filter_sleep():
    return "filter 설정"


# 검색 조회 - 해당 필터값을 기반으로 조회
@router.get("/filter")
async def get_users_by_filter():
    return ""



