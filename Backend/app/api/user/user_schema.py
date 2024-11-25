import re

from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class LoginUser(BaseModel):
    email: EmailStr
    passkey: str
    
    @field_validator('email', 'passkey')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator("email")
    def not_skku_email(cls, v):
        if not re.match("^[a-zA-Z0-9._%+-]+@(g\.)?skku\.edu$", v):
            raise ValueError('\'@g.skku.edu\' 나 \'@skku.edu\'만 사용할 수 있습니다.')
        return v
    
class RegisterUser(BaseModel):
    email:              EmailStr
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
    isOpenAge:          bool
    isOpenMajor:        bool

    @field_validator('email', 'username', 'dormitory', 'latestGPA', 'age', 'semester', 'major', 'selfIntroduction', 'weekendProportion', 'isOpenAge', 'isOpenMajor')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator('trait')
    def not_empty_traits(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class GenTokenUser(BaseModel):
    email: EmailStr
    
    @field_validator("email")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator("email")
    def not_skku_email(cls, v):
        if not re.match("^[a-zA-Z0-9._%+-]+@(g\.)?skku\.edu$", v):
            raise ValueError('\'@g.skku.edu\' 나 \'@skku.edu\'만 사용할 수 있습니다.')
        return v
    
class VerifyTokenUser(BaseModel):
    email: EmailStr
    

class ModifyUserInfo(BaseModel):
    uid:                str
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
    isOpenAge:          bool
    isOpenMajor:        bool
    isBasicInfoEntered: bool

    @field_validator('username', 'dormitory', 'latestGPA', 'age', 'semester', 'major', 'selfIntroduction', 'weekendProportion', 'isOpenAge', 'isOpenMajor')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator('trait')
    def not_empty_traits(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class ModifyUserInfoName(BaseModel):
    uid: str
    username: str
    
    @field_validator("uid", "username")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v