from beanie import Document, Link
from typing import Optional

from app.models.users import User

class UserSettings(Document):
    # id: int
    isOpenAge: Optional[bool] = False
    isOpenMajor: Optional[bool] = False
    isBasicInfoEntered: Optional[bool] = False
    userId: Optional[Link[User]]

    class Settings:
        collection = "UserSettings"