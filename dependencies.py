from functools import lru_cache

from redis.client import Redis
from urllib import parse
from settings import Settings


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def get_redis() -> Redis:
    url = parse.urlparse(get_settings().REDIS_URL)
    return Redis(host=url.hostname)
