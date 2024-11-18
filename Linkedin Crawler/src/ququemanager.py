import redis

class QueueManager:
    def __init__(self):
        self.queue = redis.StrictRedis(host='localhost', port=6379, db=0)

    def push_url(self, url):
        self.queue.rpush('linkedin_urls', url)

    def pop_url(self):
        return self.queue.lpop('linkedin_urls')
