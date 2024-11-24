from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    uid: Optional[str]
    email: str
    passkey: Optional[str]
    passkeySentTime: datetime = Field(default_factory=datetime.utcnow)
    username: str

    model_config = ConfigDict(from_attributes=True)