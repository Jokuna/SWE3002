from pydantic import BaseModel, ConfigDict
from typing import Optional

class ChatRoom(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)