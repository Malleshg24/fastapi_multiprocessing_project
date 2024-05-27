from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_lists_endpoint():
    response = client.post("/add/", json={"lists": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    assert response.json() == {"sums": [3, 7]}

    response = client.post("/add/", json={"lists": [[]]})
    assert response.status_code == 200
    assert response.json() == {"sums": [0]}

    response = client.post("/add/", json={"lists": [[1, "a"], [3, 4]]})
    assert response.status_code == 422
