from beanie import Document, Link
from typing import Optional
from datetime import datetime

from app.models.users import User
from app.models.chatrooms import ChatRoom

class Chat(Document):
    # id: int
    userId1: str # Optional[Link[User]]  # 사용자 1 ID
    userId2: str # Optional[Link[User]]  # 사용자 2 ID
    chatRoomId: str # 채팅방 ID
    created_at: datetime = datetime.utcnow()

    class Settings:
        collection = "Chats"