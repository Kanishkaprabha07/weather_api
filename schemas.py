from pydantic import BaseModel, Field
from datetime import date

class WeatherRequest(BaseModel):
    city: str 
    date: date 

class WeatherResponse(BaseModel):
    city: str
    date: date
    temperature: float
    humidity: int
    wind_speed: float
    
