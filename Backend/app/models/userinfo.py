from beanie import Document, Link
from typing import Optional, List

from app.models.users import User

class UserInfo(Document):
    # id: int
    isMale: bool
    dormitary: Optional[int] = 0
    latestGPA: float
    isSmoke: Optional[bool] = False
    sleepingTime: str
    wakeTime: str
    age: int
    semester: int
    major: str
    selfIntroduction: Optional[str] = None
    trait: Optional[List[str]] = None  # 특성 배열
    weekendProportion: Optional[int] = None

    userId: Optional[Link[User]]

    class Settings:
        collection = "UserInfo"