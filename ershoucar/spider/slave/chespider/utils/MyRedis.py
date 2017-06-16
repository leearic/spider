import redis

from chespider import settings

class Redis_MQ(object):
    def __init__(self):
        self.r = redis.StrictRedis(host=settings.Redis_HOST, port=settings.Redis_PORT, db=0, password=None)

    def get(self, key):
        return self.r.rpop(key)
    def set(self, key, value):
        # self.r.set(key, value)
        self.r.rpush(key, value)
