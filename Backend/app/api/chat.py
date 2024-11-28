from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from bson.json_util import dumps
import json
from jose import jwt
from typing import List

from app.db import get_db
from app.api.user.user_schema import *
from app.models import *
from app.api.user.jwt import SECRET_KEY, ALGORITHM

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
@router.post("/create")
async def create_chat_room(_user: ModifyUserInfoName, target_user_id: str,
    db: AsyncIOMotorDatabase=Depends(get_db)):

    # Name은 안씀
    my_id =  _user.token["sub"]

    # 1. 권한 확인
    existing_user = await db["User"].find_one({ "_id": ObjectId(my_id)})
    if not existing_user:
        raise HTTPException(status_code=403, detail="User does not exist")

    # 2. 상대방 유저의 존재 확인
    existing_target_user = await db["User"].find_one({ "_id": ObjectId(target_user_id)})
    if not existing_target_user:
        raise HTTPException(status_code=404, detail="Partner does not exist")

    # 2.1 이미 존재하는 채팅방인지 확인

    # 3. 채팅방 개설
    chatroom = ChatRoom()
    await chatroom.insert()

    chat = Chat(userId1=ObjectId(my_id), userId2=ObjectId(target_user_id), chatRoomId=str(chatroom.id))
    await chat.insert()

    return {
        "msg": "Chat room created successfully",
        "chatroom_id": str(chatroom.id),
        "participants": [
            {"user_id": my_id},
            {"user_id": target_user_id}
        ]
    }


# 채팅방 내역 조회
@router.get("/history/{chatroom_id}")
async def get_chatroom_history(chatroom_id: str, db: AsyncIOMotorDatabase=Depends(get_db)):

    existing_chatroom = await db["ChatRoom"].find_one({ "_id": ObjectId(chatroom_id)})
    if not existing_chatroom:
        raise HTTPException(status_code=404, detail="ChatRoom does not exist")

    existing_chat = await db["Chat"].find_one({ "chatRoomId": str(chatroom_id)}) # existing_chatroom["_id"]
    if not existing_chat:
        raise HTTPException(status_code=404, detail="Chat does not exist")

    # 채팅창 내역 전부 가져오기
    messages_cursor = db["Messages"].find({ "chatId": str(existing_chat["_id"]) })
    messages = await messages_cursor.to_list(length=None)
    messages_json = dumps(messages)
    
    dictionary = json.loads(messages_json)
    return dictionary
    
# 채팅 전송
@router.post("/message/{chatroom_id}")
async def send_chat_message(chatroom_id: str, _user: ModifyUserInfoName, msg: str, db: AsyncIOMotorDatabase=Depends(get_db)):

    my_id =  _user.token["sub"]
    
    # 1. 권한 확인
    existing_user = await db["User"].find_one({ "_id": ObjectId(my_id)})
    if not existing_user:
        raise HTTPException(status_code=403, detail="User does not exist")

    # 2. 채팅방이 존재하는지 확인
    existing_chatroom = await db["ChatRoom"].find_one({ "_id": ObjectId(chatroom_id)})
    if not existing_chatroom:
        raise HTTPException(status_code=404, detail="ChatRoom does not exist")

    existing_chat = await db["Chat"].find_one({ "chatRoomId": chatroom_id})
    if not existing_chat:
        raise HTTPException(status_code=404, detail="Chat does not exist")

    # 3. 메세지 전송
    message = Messages(writerId=ObjectId(my_id), text=msg, chatId=str(existing_chat["_id"]))
    await message.insert()

    return {"msg": "Message sent successfully", "chatroom_id": chatroom_id}

# 신규 메시지 알림 ... 
