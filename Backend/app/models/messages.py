from beanie import Document, Link
from datetime import datetime
from typing import Optional

from app.models.users import User
from app.models.chats import Chat

class Messages(Document):
    # id: int
    writerId: Optional[Link[User]] # Optional[int]  # 작성자 ID
    text: str
    writeTime: datetime = datetime.utcnow()
    chatId: Optional[Link[Chat]] # chat 그룹은 알아야지

    class Settings:
        collection = "Messages"