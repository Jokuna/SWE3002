from beanie import Document
from datetime import datetime
from typing import Optional

class User(Document):
    # id: int
    uid: Optional[str]
    email: str
    passkey: Optional[str]
    passkeySentTime: datetime = datetime.utcnow()
    username: str
    similarity: Optional[int]

    class Settings:
        collection = "Users"