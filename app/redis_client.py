import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def set_cache(key, value, ttl=30):
    redis_client.setex(key, ttl, value)

def get_cache(key):
    return redis_client.get(key)
