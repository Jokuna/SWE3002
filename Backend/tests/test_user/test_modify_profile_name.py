import asyncio 
from httpx import AsyncClient
from datetime import datetime, timedelta

import pytest
import pytest_asyncio 
from unittest.mock import AsyncMock, patch
from bson import ObjectId
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

userId: str = "674454955eb317081ff2b3af"
@pytest.fixture
def token():
    token = jwt.encode({
        "sub": userId, 
        "exp": datetime.now() + timedelta(hours=24)}, 
        SECRET_KEY, algorithm=ALGORITHM)
    
    return token

'''
API test

Template...
@pytest.mark.asyncio
async def test_modify_profile_name(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
'''
@pytest.mark.asyncio
async def test_modify_profile_name_sucess(mock_db: AsyncMock, client: AsyncClient, token):
    mock_collection = AsyncMock()
    mock_collection.update_one = AsyncMock(return_value=AsyncMock(modified_count=1))
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    userinfo = {
        "token": token,
        "username": "new_username"
    }
    
    response = await client.post("/backend/user/profile/name", json=userinfo)
    
    assert response.status_code == 200
    assert response.json() == {"msg": "User name updated successfully"}
    
@pytest.mark.asyncio
async def test_modify_profile_name_user_not_found(mock_db: AsyncMock, client: AsyncClient, token: str):
    mock_collection = AsyncMock()
    mock_collection.update_one.modified_count = AsyncMock(return_value=AsyncMock(modified_count=0))
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    userinfo = {
        "token": token,
        "username": "new_username"
    }
    
    response = await client.post("/backend/user/profile/name", json=userinfo)
    
    assert response.status_code == 401
    assert response.json() == {"detail": "User not found or name not modified"}
    
@pytest.mark.asyncio
async def test_modify_profile_name_invalid_userinfo(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.update_one.modified_count = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    userinfo = {
        "token": "invalid_token",
        "username": "new_username"
    }
    
    response = await client.post("/backend/user/profile/name", json=userinfo)
    
    assert response.status_code == 422
    assert response.json() ==   {
        'detail': [
            {'ctx': {'error': {}},
            'input': 'invalid_token',
            'loc': ['body', 'token'],
            'msg': 'Value error, Invalid token',
            'type': 'value_error'}
        ]
    }