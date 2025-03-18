import requests
from config import OPENWEATHER_API_KEY
import json
from config import redis_client
from schemas import WeatherResponse
class WeatherReport:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self,city:str , date: str):  
        
        cache_key = f"{city}:{date}"
        cached_data = redis_client.get(cache_key)
        if cached_data:
            print("from cache")
            return WeatherResponse(**json.loads(cached_data))
        url = self.base_url +"?q=" +city+ "&appid=" + OPENWEATHER_API_KEY
        response = requests.get(url)
        result=response.json()
        print (response)
        
        if result.get("cod") != 200:
            raise ValueError
        data ={
        "city":city,
        "date":str(date),
        "temperature":result["main"]["temp"],
        "humidity":result["main"]["humidity"],
        "wind_speed":result["wind"]["speed"]
        }
  
        redis_client.setex(cache_key, 3600, json.dumps(data))  
        return WeatherResponse(**data)



    
    
    