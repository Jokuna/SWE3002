
from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class LoginUser(BaseModel):
    email: EmailStr
    passkey: str
    
class RegisterUser(BaseModel):
    username:           str
    isMale:             bool
    dormitory:          int
    latestGPA:          float
    isSmoke:            bool
    sleepingTime:       str
    wakeTime:           str
    age:                int
    semester:           int
    major:              str
    selfIntroduction:   str
    trait:              list[str]
    weekendProportion:  int

    @field_validator('username', 'dormitory', 'latestGPA', 'age', 'semester', 'major', 'selfIntroduction', 'weekendProportion')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator('trait')
    def not_empty_list(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class ModifyUserInfo(BaseModel):
    ...