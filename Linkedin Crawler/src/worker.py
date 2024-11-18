from scraper import LinkedInScraper
from ququemanager import QueueManager
from database import DataStorageHandler

class Worker:
    def __init__(self):
        self.scraper = LinkedInScraper()
        self.queue = QueueManager()
        self.storage = DataStorageHandler()

    def run(self):
        while True:
            url = self.queue.pop_url()
            if url:
                posts = self.scraper.scrape_posts(url)
                for post in posts:
                    self.storage.insert_post(post)
                profiles = self.scraper.discover_profiles(url)
                for profile in profiles:
                    self.queue.push_url(profile)
