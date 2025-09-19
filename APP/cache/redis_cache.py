import json
import redis 
from APP.Core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key:str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cached_pediction(key: str, value:dict, expiry: int = 3600):
    redis_client.setex(key,expiry,json.dumps(value))
    