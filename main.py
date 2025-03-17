from fastapi import FastAPI
import redis
from config import REDIS_URL

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Weather API is running"}
