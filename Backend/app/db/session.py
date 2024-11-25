from typing import AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import ChatRoom, Chat, Messages, UserInfo, User, UserSettings


# MongoDB 연결 설정
MONGO_URI = "mongodb://admin:adminpass@localhost:27017"
DATABASE_NAME = "mydatabase"

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client[DATABASE_NAME], document_models=[
        ChatRoom,
        Chat,
        Messages,
        UserInfo,
        User,
        UserSettings,
    ])
    
client = AsyncIOMotorClient(MONGO_URI)
async def get_db() -> AsyncGenerator:
    try:
        yield client[DATABASE_NAME]
    finally:
        # 연결을 닫는 작업이 필요하면 추가
        pass