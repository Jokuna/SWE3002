import asyncio 
from httpx import AsyncClient

import pytest
import pytest_asyncio 
from unittest.mock import AsyncMock

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
getToken Test
'''
@pytest.mark.asyncio 
async def test_genToken_existing_user(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={"email": "test@skku.edu"})
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db

    response = await client.post("/backend/user/genToken", json={"email": "test@skku.edu"})
    
    assert response.status_code == 200
    assert response.json() == {"msg": "Successfully send passkey"}

@pytest.mark.asyncio 
async def test_genToken_new_user(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None

    response = await client.post("/backend/user/genToken", json={"email": "test@skku.edu"})
    
    assert response.status_code == 200
    assert response.json() == {"msg": "Successfully send passkey"}
    
@pytest.mark.asyncio 
async def test_genToken_blank_email(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    response = await client.post("/backend/user/genToken", json={"email": ""})
    
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
            }
        ]
    }
    
@pytest.mark.asyncio 
async def test_genToken_unvalid_email(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "User" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    response = await client.post("/backend/user/genToken", json={"email": "test@example.com"})
    
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "type": "value_error",
            "loc": [
                "body",
                "email"
            ],
            "msg": "Value error, '@g.skku.edu' 나 '@skku.edu'만 사용할 수 있습니다.",
            "input": "test@example.com",
            "ctx": {
                "error": {}
            }
            }
        ]
    }
