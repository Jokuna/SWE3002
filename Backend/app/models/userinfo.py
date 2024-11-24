from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class UserInfo(BaseModel):
    id: int
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

    model_config = ConfigDict(from_attributes=True)