import pytest
from app import app  # Import your Flask app from the main file

@pytest.fixture
def client():
    # This fixture provides a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_home(client):
    # Test the root route '/'
    response = client.get("/")
    assert response.status_code == 200  # Check if the response status is 200 (OK)
    assert response.data == b"Hello, World!"  # Check if the response data matches the expected text
