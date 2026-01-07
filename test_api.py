import pytest
from fastapi.testclient import TestClient
from main_api import app, users, items

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_data():
    """Reset data before each test"""
    users.clear()
    items.clear()
    from main_api import user_id_counter, item_id_counter
    yield


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_user():
    response = client.post(
        "/users",
        json={"name": "John Doe", "email": "john@example.com", "age": 30}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["age"] == 30
    assert "id" in data


def test_get_user():
    # Create a user first
    create_response = client.post(
        "/users",
        json={"name": "Jane Doe", "email": "jane@example.com", "age": 25}
    )
    user_id = create_response.json()["id"]
    
    # Get the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_list_users():
    # Create two users
    client.post("/users", json={"name": "User1", "email": "user1@example.com", "age": 20})
    client.post("/users", json={"name": "User2", "email": "user2@example.com", "age": 30})
    
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_create_item():
    response = client.post(
        "/items",
        json={"name": "Laptop", "description": "Gaming laptop", "price": 1200.50}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 1200.50


def test_get_item():
    # Create an item first
    create_response = client.post(
        "/items",
        json={"name": "Phone", "description": "Smartphone", "price": 800.0}
    )
    item_id = create_response.json()["id"]
    
    # Get the item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Phone"


def test_get_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_delete_item():
    # Create an item first
    create_response = client.post(
        "/items",
        json={"name": "Mouse", "description": "Wireless mouse", "price": 25.99}
    )
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"


def test_delete_nonexistent_item():
    response = client.delete("/items/999")
    assert response.status_code == 404


def test_create_user_invalid_age():
    # Test validation error when sending string age instead of int
    response = client.post(
        "/users",
        json={"name": "Test User", "email": "test@example.com", "age": "thirty"}
    )
    assert response.status_code == 422  # Fixed: Expect 422 for validation error


def test_multiple_items_creation():
    response1 = client.post("/items", json={"name": "Item1", "description": "Desc1", "price": 10.0})
    response2 = client.post("/items", json={"name": "Item2", "description": "Desc2", "price": 20.0})
    
    assert response1.json()["id"] != response2.json()["id"]


def test_user_email_field():
    response = client.post(
        "/users",
        json={"name": "Email Test", "email": "email@test.com", "age": 28}
    )
    assert response.json()["email"] == "email@test.com"
