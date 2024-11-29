import asyncio 
from httpx import AsyncClient
from datetime import datetime, timedelta

import pytest
import pytest_asyncio 
from unittest.mock import AsyncMock, patch
from jose import jwt

from app.main import app
from app.db import get_db
from app.api.user.jwt import SECRET_KEY, ALGORITHM

'''
기본 기능 설정
'''
# Mock 데이터베이스와 의존성 
@pytest.fixture(scope="function")
def mock_db():
    return AsyncMock()

@pytest_asyncio.fixture(scope="function")
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
            yield client

@pytest.fixture(scope="session")
def event_loop():
    # 새 이벤트 루프를 생성
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
    
@pytest.fixture
def token():
    token = jwt.encode({
        "sub": "674454955eb317081ff2b3af", 
        "exp": datetime.now() + timedelta(hours=24)}, 
        SECRET_KEY, algorithm=ALGORITHM)
    
    return token

'''
API test

Template...
@pytest.mark.asyncio
async def test_modify_profile(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
'''
@pytest.mark.asyncio
async def test_modify_profile_success(mock_db: AsyncMock, client: AsyncClient, token: str):
    mock_collection = AsyncMock()
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    user_data = {
        "token": token,
        "username": "new_username",
        "isMale": True,
        "dormitory": 1,
        "latestGPA": 3.5,
        "isSmoke": False,
        "sleepingTime": "22:00",
        "wakeTime": "06:00",
        "age": 20,
        "semester": 3,
        "major": "Computer Science",
        "selfIntroduction": "Hello, I'm a student.",
        "trait": ["Curious"],
        "weekendProportion": 2,
        "isOpenAge": True,
        "isOpenMajor": False
    }
    
    response = await client.post("/backend/user/profile", json=user_data)
    
    assert response.status_code == 200
    assert response.json() == {"msg": "UserInfo updated successfully"}
    
@pytest.mark.asyncio
async def test_modify_profile_invalid_userinfo(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    user_data = {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NzQ3MWUzNzk2MzU4ODIzZDIxNDI3ZTUiLCJleHAiOjE3MzMwMDIwNzZ9.oPSCBZj4dqulSeOQL7O0FcWUMiqud8T0A23OCRlfrIw",
        "username": "",
        "isMale": True,
        "dormitory": 0,
        "latestGPA": 0.0,
        "isSmoke": False,
        "sleepingTime": "",
        "wakeTime": "",
        "age": 0,
        "semester": 0,
        "major": "",
        "selfIntroduction": "",
        "trait": [],
        "weekendProportion": 0,
        "isOpenAge": True,
        "isOpenMajor": False
    }
    
    response = await client.post("/backend/user/profile", json=user_data)
    
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {'ctx': {'error': {}},
            'input': '',
            'loc': ['body', 'username'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': 0,
            'loc': ['body', 'dormitory'],
            'msg': 'Value error, 0은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': 0.0,
            'loc': ['body', 'latestGPA'],
            'msg': 'Value error, GPA는 0.0이 될 수 없습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': '',
            'loc': ['body', 'sleepingTime'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': '',
            'loc': ['body', 'wakeTime'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': 0,
            'loc': ['body', 'age'],
            'msg': 'Value error, 0은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': 0,
            'loc': ['body', 'semester'],
            'msg': 'Value error, 0은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': '',
            'loc': ['body', 'major'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': '',
            'loc': ['body', 'selfIntroduction'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'},
            {'ctx': {'error': {}},
            'input': [],
            'loc': ['body', 'trait'],
            'msg': 'Value error, 빈 값은 허용되지 않습니다.',
            'type': 'value_error'}
        ]
    }
    
@pytest.mark.asyncio
async def test_modify_profile_invalid_token(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    
    user_data = {
        "token": "invalid_token",
        "username": "new_username",
        "isMale": True,
        "dormitory": 1,
        "latestGPA": 3.5,
        "isSmoke": False,
        "sleepingTime": "22:00",
        "wakeTime": "06:00",
        "age": 20,
        "semester": 3,
        "major": "Computer Science",
        "selfIntroduction": "Hello, I'm a student.",
        "trait": ["Curious"],
        "weekendProportion": 2,
        "isOpenAge": True,
        "isOpenMajor": False
    }
    
    response = await client.post("/backend/user/profile", json=user_data)
    
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "type": "value_error",
            "loc": [
                "body",
                "token"
            ],
            "msg": "Value error, Invalid token",
            "input": "invalid_token",
            "ctx": {
                "error": {}
            }
            }
        ]
    }