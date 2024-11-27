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
'''

'''
Login test
'''
@pytest.mark.asyncio
async def test_login_success(mock_db: AsyncMock, client: AsyncClient):
    # Mock 데이터 설정
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={
        "_id": "mock_user_id",
        "email": "test@skku.edu",
        "passkey": "123456",
        "username": "Test User",
    })
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    response = await client.post(
        "/backend/user/login",
        json={"email": "test@skku.edu", "passkey": "123456",}
    )
    
    # 응답 확인
    assert response.json() == {
        "message": "Login successful",
        "user": {
            "_id": "mock_user_id",
            "email": "test@skku.edu",
            "passkey": "123456",
            "username": "Test User",
        }
    }
    assert response.status_code == 200
    # 세션 쿠키 확인
    assert "session_id" in response.cookies


@pytest.mark.asyncio
async def test_login_invalid_credentials(mock_db: AsyncMock, client: AsyncClient):
    # Mock 데이터베이스: 사용자 없음
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    # API 호출
    response = await client.post(
        "/backend/user/login", 
        json={"email": "test@skku.edu", "passkey": "wrong_passkey"}
    )

    # 응답 확인
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid email"}
    
@pytest.mark.asyncio
async def test_login_invalid_passkey(mock_db: AsyncMock, client: AsyncClient):
    # Mock 데이터베이스: 사용자 없음
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={
        "_id": "mock_user_id",
        "email": "test@skku.edu",
        "passkey": "123456",
        "username": "Test User",
    })
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None
    app.dependency_overrides[get_db] = lambda: mock_db
    
    # API 호출
    response = await client.post(
        "/backend/user/login", 
        json={"email": "test@skku.edu", "passkey": "wrong_passkey"}
    )

    # 응답 확인
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid passkey"}

'''
getToken Test
'''
@pytest.mark.asyncio 
async def test_genToken_existing_user(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value={"email": "test@skku.edu"})
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None
    app.dependency_overrides[get_db] = lambda: mock_db

    response = await client.post("/backend/user/genToken", json={"email": "test@skku.edu"})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully send passkey"}

@pytest.mark.asyncio 
async def test_genToken_new_user(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None

    response = await client.post("/backend/user/genToken", json={"email": "test@skku.edu"})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully send passkey"}
    
@pytest.mark.asyncio 
async def test_genToken_unvalid_email(mock_db: AsyncMock, client: AsyncClient):
    mock_collection = AsyncMock()
    mock_collection.find_one = AsyncMock(return_value=None)
    mock_db.__getitem__.side_effect = lambda key: mock_collection if key == "users" else None
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

