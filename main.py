from time import time
from typing import Union

from fastapi import Depends, FastAPI
from redis.client import Redis

from dependencies import get_redis
from schemas import RedisRecord

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/redis/")
async def insert_into_redis(record: RedisRecord, redis: Redis = Depends(get_redis)):
    now = int(time() * 1000)
    redis.set(record.post_id, now)
    return {"status": "Success", "post_id": record.post_id, "value": now}


@app.get("/redis/{post_id}")
async def get_from_redis(post_id: Union[str, int], redis: Redis = Depends(get_redis)):
    value = redis.get(post_id)
    return {"post_id": post_id, "value": value}
