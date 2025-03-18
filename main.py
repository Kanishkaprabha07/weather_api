from fastapi import FastAPI
import redis
from config import REDIS_URL
from schemas import WeatherRequest, WeatherResponse  
from service import WeatherReport
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Weather API is now running"}

@app.post("/weather")
def get_weather(request: WeatherRequest):
    result = WeatherReport()
    return result.get_weather(request.city,request.date)
