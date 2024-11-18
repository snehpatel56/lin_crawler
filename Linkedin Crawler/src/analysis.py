import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('scraper.db')
lin_post = pd.read_sql_query("SELECT * FROM posts", conn)


# Average Monthly Posting Frequency
lin_post = pd.to_datetime(lin_post['date'])
post_per_month = lin_post.groupby(lin_post['date'].dt.to_period('M')).size()
print("Average Monthly Frequency:", post_per_month.mean())


# Average Post Length
lin_post["content_length"]  = lin_post["content"].str.len()
avg_lin_post_length = lin_post["content_length"].mean()


# Average number of Likes on each Media Element (Posts with Image/Video) - [Bar Graph]
media_likes = lin_post.groupby("media_type")["Likes"].mean()
media_likes.plot(kind="bar",title = "Average Likes by Media")


# Average number of Comments on each Media Element (Posts with Image/Video)- [Bar Graph]
media_likes = lin_post.groupby("media_type")["Likes"].mean()
media_likes.plot(kind="bar",title = "Average Likes by Media")