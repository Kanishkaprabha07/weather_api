from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_get_weather():
    input = {"city" :"Palani","date" : "2025-10-02"}
    response= client.post("/weather",json=input)
    assert response.status_code==200
    assert response.json()
    
