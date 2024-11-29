import asyncio 
from httpx import AsyncClient

import pytest
import pytest_asyncio 
from unittest.mock import AsyncMock, patch
from bson import ObjectId

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
async def test_get_profile(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
'''
@pytest.mark.asyncio
async def test_get_profile_success(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={
        "_id": ObjectId("674454955eb317081ff2b3af"),
        "email": "test@skku.edu",
        "passkey": "123456"
    })
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    response = await client.get(f"backend/user/profile/674454955eb317081ff2b3af")
    
    assert response.status_code == 200
    assert response.json() == {'_id': '674454955eb317081ff2b3af', 'email': 'test@skku.edu'}

@pytest.mark.asyncio
async def test_get_profile_invalid_userId(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    response = await client.get(f"backend/user/profile/674454955eb317081ff2b3af")
    
    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid user id'}