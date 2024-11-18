LinkedIn Crawler and Data Analysis System

This project is a LinkedIn crawler designed to scrape at least 500 LinkedIn posts and analyze posting behavior.
The system is built using Python, adheres to object-oriented principles, and includes distributed queue processing for efficient scraping. Analytical tasks are performed using a Jupyter Notebook.

Features:

Scrapes LinkedIn posts from user profiles.
Recursively collects and processes profile URLs using a distributed queue.
Stores scraped data in a database.
Provides insights through data analysis, including:
Average monthly posting frequency.
Average post length.
Bar graphs for average likes and comments on media posts.
Additional metrics for LinkedIn posting behavior.



Architecture

Scraper: Extracts posts and collects new profile URLs.
Queue System: Uses Redis/Kafka to manage URL processing.
Workers: Concurrent scraping processes for efficiency.
Database: Stores crawled data for later analysis.
Analysis: Performed in a Jupyter Notebook with data visualizations.


Setup Instructions

1. Prerequisites
Python 3.9+
Docker
Poetry
Redis (for queue management)


2. Installation

1) Clone the repository:

git clone <repository-url>
cd linkedin_crawler

2) Set up environment variables in a .env file:
python -m venv .venv

.\.venv\Scripts\activate

if this gets error then you can type this
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\.venv\Scripts\activate   it will Works now


pip install -r requirement.txt



LINKEDIN_USERNAME=your_email
LINKEDIN_PASSWORD=your_password
REDIS_URL=redis://localhost:6379
DATABASE_URL=sqlite:///linkedin_crawler.db 


4) Start the Redis server:
redis-server

5) Running the Application
 i) Start Workers
poetry run python crawler/worker.py


ii) Scrape Profiles: Push a LinkedIn profile URL to the queue
from crawler.queue_handler import QueueHandler
queue = QueueHandler()
queue.push("https://www.linkedin.com/in/example-profile/")



5)Data Analysis
 we will use analysis.py for it

our Metrics Computed:

Average monthly posting frequency.
Average post length.
Bar graphs for average likes and comments per media type.


6) Docker Deployment:

i) Build the Docker image:

docker build -t linkedin_crawler


ii)
docker run --env-file .env linkedin_crawler