from time import time

from fastapi import Depends, FastAPI
from redis.client import Redis

from dependencies import get_redis

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/redis/")
async def insert_into_redis(post_id: str, redis: Redis = Depends(get_redis)):
    now = int(time() * 1000)
    redis.set(post_id, now)
    return {"status": "Success", "value": now}


@app.get("/redis/{post_id}")
async def get_from_redis(post_id: str, redis: Redis = Depends(get_redis)):
    value = redis.get(post_id)
    return {"post_id": post_id, "value": value}
