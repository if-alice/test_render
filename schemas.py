from typing import Union

from pydantic import BaseModel


class RedisRecord(BaseModel):
    post_id: Union[str, int]
