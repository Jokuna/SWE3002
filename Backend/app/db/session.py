from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import ChatRoom, Chat, Messages, UserInfo, User, UserSettings


# MongoDB 연결 설정
MONGO_URI = "mongodb://localhost:27017"
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