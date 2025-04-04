from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch,Mock
from service import WeatherReport
from config import OPENWEATHER_API_KEY
client = TestClient(app)
def test_get_weather():
    input = {"city" :"Palani","date" : "2025-10-02"}
    response= client.post("/weather",json=input)
    assert response.status_code==200
    assert response.json()
   
@patch('service.WeatherReport.get_weather')
def test_get_weather_func(mock_get_weather):
    mock_response = {
        "cod": 200,
        "main": {"temp": 70, "humidity": 20},
        "wind": {"speed": 100}
    }
    mock_get_weather.return_value = mock_response
    input = {"city" :"Palani","date" : "2025-10-02"}
    response = client.post("/weather",json=input)

    assert response.status_code == 200
    assert response.json()["main"]["temp"] == 70

@patch('requests.get')
def test_request_get(mock_request_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "cod": 200,
        "main": {"temp": 70, "humidity": 20},
        "wind": {"speed": 100}
    }
    mock_request_get.return_value = mock_response
    weather_report = WeatherReport()
    city ="bombay"
    weather_report.get_weather(city, "2024-04-07")
    input = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    mock_request_get.assert_called_with(input)
