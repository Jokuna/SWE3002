from beanie import Document
from datetime import datetime

class ChatRoom(Document):
    # id: int

    class Settings:
        collection = "ChatRoom"