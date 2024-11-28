from datetime import datetime

import re

from jose import jwt, JWTError
from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo
from app.api.user.jwt import SECRET_KEY, ALGORITHM

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

class RegisterUser_passkey(RegisterUser):
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
    token:              str
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
    
    @field_validator("token")
    def validate_token(cls, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if payload.get("exp") < datetime.now().timestamp():
                raise ValueError("Token has expired")
            return payload  # 반환값은 다음 단계에서 사용할 수 있음
        except JWTError:
            raise ValueError("Invalid token")

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
    token: str
    username: str
    
    @field_validator("token")
    def validate_token(cls, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if payload.get("exp") < datetime.now().timestamp():
                raise ValueError("Token has expired")
            return payload  # 반환값은 다음 단계에서 사용할 수 있음
        except JWTError:
            raise ValueError("Invalid token")
    
    @field_validator("username")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v