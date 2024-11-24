from fastapi import APIRouter, Depends
from typing import List

'''
채팅 API
'''
router = APIRouter(
    prefix="/backend/chat",
    tags=["chat"]
)

@router.get("/")
async def hello():
    return "Hello World"

# 채팅방 생성
@router.post("/gen")
async def get_user_info():
    return "get_user_info"


# 채팅방 내역 조회
@router.get("/history/{chat_id}")
async def get_chat_history():
    return "get_chat_history"

# 채팅 전송
@router.post("/message/{user_id}")
async def send_chat_message():
    return "send_chat_message"

# 신규 메시지 알림 ... 
