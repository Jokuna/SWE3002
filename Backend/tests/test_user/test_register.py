import asyncio 
from httpx import AsyncClient

import pytest
import pytest_asyncio 
from unittest.mock import AsyncMock, patch

from app.main import app
from app.db import get_db

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

'''
API test

Template...
@pytest.mark.asyncio
async def test_register(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
'''

@pytest.mark.asyncio
async def test_register_existing_user(mock_db: AsyncMock, client: AsyncClient):
    # Mock 데이터 설정
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={
        "_id": "mock_user_id",
        "email": "test@skku.edu",
        "passkey": "123456",
    })
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    # 기존 사용자 데이터 설정
    user_data = {
        "email": "test@skku.edu",
        "passkey": "testpass",
        "username": "testuser",
        "isMale": True,
        "dormitory": 1,
        "latestGPA": 3.5,
        "isSmoke": False,
        "sleepingTime": "22:00",
        "wakeTime": "06:00",
        "age": 20,
        "semester": 2,
        "major": "Computer Science",
        "selfIntroduction": "Hello!",
        "trait": ["Friendly"],
        "weekendProportion": 0,
        "isOpenAge": True,
        "isOpenMajor": True
    }

    response = await client.post("/backend/user/register", json=user_data)
    
    assert response.status_code == 200
    assert response.json() == {"msg": "User updated successfully"}

@pytest.mark.asyncio
async def test_register_non_existing_user(mock_db: AsyncMock, client: AsyncClient):
    # Mock 데이터 설정
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    # 기존 사용자 데이터 설정
    user_data = {
        "email": "test@skku.edu",
        "passkey": "testpass",
        "username": "testuser",
        "isMale": True,
        "dormitory": 1,
        "latestGPA": 3.5,
        "isSmoke": False,
        "sleepingTime": "22:00",
        "wakeTime": "06:00",
        "age": 20,
        "semester": 2,
        "major": "Computer Science",
        "selfIntroduction": "Hello!",
        "trait": ["Friendly"],
        "weekendProportion": 0,
        "isOpenAge": True,
        "isOpenMajor": True
    }

    response = await client.post("/backend/user/register", json=user_data)
    
    assert response.status_code == 404
    assert response.json() == {'detail': 'User does not exist'}
    
@pytest.mark.asyncio
async def test_register_blank_validation(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
        # 기존 사용자 데이터 설정
    user_data = {
        "email": "",
        "passkey": "",
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
        "isOpenMajor": True
    }

    response = await client.post("/backend/user/register", json=user_data)
    
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "type": "value_error",
            "loc": [
                "body",
                "email"
            ],
            "msg": "value is not a valid email address: An email address must have an @-sign.",
            "input": "",
            "ctx": {
                "reason": "An email address must have an @-sign."
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "passkey"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "username"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "dormitory"
            ],
            "msg": "Value error, 0은 허용되지 않습니다.",
            "input": 0,
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "sleepingTime"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "wakeTime"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "age"
            ],
            "msg": "Value error, 0은 허용되지 않습니다.",
            "input": 0,
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "semester"
            ],
            "msg": "Value error, 0은 허용되지 않습니다.",
            "input": 0,
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "major"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "selfIntroduction"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": "",
            "ctx": {
                "error": {}
            }
            },
            {
            "type": "value_error",
            "loc": [
                "body",
                "trait"
            ],
            "msg": "Value error, 빈 값은 허용되지 않습니다.",
            "input": [],
            "ctx": {
                "error": {}
            }
            }
        ]
    }