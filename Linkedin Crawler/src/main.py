import poetry
from poetry import redis
from poetry import requests
from poetry import flask

from src.ququemanager import QueueManager
from src.crawler import Crawler
from src.database import DatabaseManager
import threading

class Worker:
    def __init__(self):
        self.queue_manager = QueueManager()
        self.db_manager = DatabaseManager()

    def run(self):
        while True:
            url = self.queue_manager.pop_url()
            if url:
                crawler = Crawler(url.decode("utf-8"))
                posts, profile_links = crawler.fetch_profile_data()
                for post in posts:
                    self.db_manager.insert_post(post)
                for link in profile_links:
                    self.queue_manager.push_url(link)

if __name__ == "__main__":
    workers = [Worker() for _ in range(2)]
    threads = [threading.Thread(target=worker.run) for worker in workers]
    for thread in threads:
        thread.start()
