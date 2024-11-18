import sqlite3

class DatabaseManager:
    def __init__(self, db_name='scraper.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                post_id INTEGER PRIMARY KEY,
                content TEXT,
                likes INTEGER,
                comments INTEGER,
                post_length INTEGER
            )
        ''')
        self.conn.commit()

    def insert_post(self, post):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO posts (post_id, content, likes, comments, post_length) VALUES (?, ?, ?, ?, ?)",
            (post["post_id"], post["content"], post["likes"], post["comments"], len(post["content"]))
        )
        self.conn.commit()
