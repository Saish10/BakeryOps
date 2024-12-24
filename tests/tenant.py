from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_tenant():
    response = client.post("/tenants/", json={"name": "Test Tenant"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Tenant"