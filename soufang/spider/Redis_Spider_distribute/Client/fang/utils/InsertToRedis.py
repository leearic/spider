import redis

class RedisSever():
    def __init__(self, host, port):
        self.r = redis.Redis(host=host, port=port)

    def push(self, url):
        self.r.lpush("url", url)
    def pop(self):
        return self.r.lpop("url")