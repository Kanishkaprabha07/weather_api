from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch


client = TestClient(app)
def test_get_weather():
    input = {"city" :"Palani","date" : "2025-10-02"}
    response= client.post("/weather",json=input)
    assert response.status_code==200
    assert response.json()
    
@patch('service.WeatherReport.get_weather')
def test_get_weather_func(mock_get_weather):
    mock_response = {
        "main": {"temp": 70, "humidity": 20},
        "wind": {"speed": 100}
    }
    mock_get_weather.return_value = mock_response
    input = {"city" :"Palani","date" : "2025-10-02"}
    response = client.post("/weather",json=input)

    assert response.status_code == 200
    assert response.json()["main"]["temp"] == 70

    
    