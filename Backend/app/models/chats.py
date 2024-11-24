from pydantic import BaseModel, ConfigDict
from typing import Optional

class Chat(BaseModel):
    id: int
    userId1: Optional[int]  # 사용자 1 ID
    userId2: Optional[int]  # 사용자 2 ID
    chatRoomId: Optional[int]  # 채팅방 ID

    model_config = ConfigDict(from_attributes=True)