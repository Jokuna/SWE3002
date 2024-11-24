from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class Messages(BaseModel):
    id: int
    writerId: Optional[int]  # 작성자 ID
    text: str
    writeTime: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)