import os
from dotenv import load_dotenv
import redis
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
