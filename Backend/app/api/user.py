from fastapi import APIRouter, Depends
from typing import List


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
async def login():
    return "login"

# 로그아웃
@router.post("/logout")
async def logout():
    return "logout"

# 회원가입
@router.post("/register")
async def register():
    return "register"

# 인증코드 생성 후, 이메일 전송
# 회원가입, 로그인 둘다 사용
@router.post("/genToken")
async def genToken():
    return "token"

# 탈퇴 .. 구현 X

'''
프로필 API
'''
# 프로필 조회
@router.get("/profile/{user_id}")
async def get_user_info():
    return "get_user_info"


# 프로필 변경
@router.post("/profile")
async def modify_user_info():
    return "modify_user_info"

# 프로필 변경 - 이름
@router.post("/profile/name")
async def modify_user_info_name():
    return "modify_user_info_name"
