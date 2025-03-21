from fastapi import FastAPI,Depends
import redis
from config import REDIS_URL
from schemas import WeatherRequest, WeatherResponse  
from service import WeatherReport
from sqlalchemy.orm import Session
from db import get_db
from sqlalchemy import text
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Weather API is now running"}

@app.post("/weather")
def get_weather(request: WeatherRequest):
    result = WeatherReport()
    return result.get_weather(request.city,request.date)

@app.get("/test_db")
def test_db(db:Session =Depends(get_db)):
    if db.execute(text('Select 1')):
        return {"msg" :" connected"}
    else:
        return {"msg" :"error"}