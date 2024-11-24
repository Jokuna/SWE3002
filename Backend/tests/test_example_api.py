from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_example_root():
    response = client.get("/backend/example")
    assert response.status_code == 200
    assert response.text == "Hello World"

def test_example_item_valid():
    response = client.get("/backend/example/1?q=example")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "example"}

def test_example_item_valid():
    response = client.get("/backend/example/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid item_id"}
