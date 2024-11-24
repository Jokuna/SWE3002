from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserSettings(BaseModel):
    id: int
    isOpenAge: Optional[bool] = False
    isOpenMajor: Optional[bool] = False
    isBasicInfoEntered: Optional[bool] = False

    model_config = ConfigDict(from_attributes=True)