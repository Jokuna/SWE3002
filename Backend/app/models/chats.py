from beanie import Document, Link
from typing import Optional
from datetime import datetime

from app.models.users import User
from app.models.chatrooms import ChatRoom

class Chat(Document):
    # id: int
    userId1: Optional[Link[User]]  # 사용자 1 ID # 이거 _di
    userId2: Optional[Link[User]]  # 사용자 2 ID
    chatRoomId: Optional[Link[ChatRoom]]  # 채팅방 ID
    created_at: datetime = datetime.utcnow()

    class Settings:
        collection = "Chats"