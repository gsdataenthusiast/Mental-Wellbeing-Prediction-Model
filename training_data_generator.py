# -*- coding: utf-8 -*-
"""Training_Data_Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YL5jJfjkDnIHgqwAfcUD7F51vtWeRogB

Given a text of user posts in an online or social networking platform, the goal is to classify the post into one among the following categories suicidal, depression, anxiety

##Training Data Generation through PRAW API
"""

!pip install praw # Install PRAW in our colab virtual machine

import praw # API for scraping subreddit data
import pandas as pd # For Data Manaipulation and Analysis
import datetime as dt # For Manipulation of Date Objects
import numpy as np # For NLP Preprocessing Operations


print("Creating instance of the Reddit class to talk to Reddit...") ## Establishing Reddit API Connection
reddit = praw.Reddit(client_id="S2kBxJViSyiFuA",
                     client_secret="Xqloqq5u-7NW76b4UudQZ7ZTddXnjQ",
                     user_agent="GRPRAW")

print("Reading 20 submissions from /r/suicidewatch...")
# Test communication with Reddit
for submission in reddit.subreddit("suicidewatch").hot(limit=20):  
    print(submission.title)

"""Webscrape Subreddit Posts on selected subreddit topics that are


*   "Top" - of all time
*   "New" - the recent ones
*   "Hot" - currently in trending


"""

subreddit_posts = []

# Naming of Variable:  SAD - "Suicidal Anxiety Depression"
# "Top" - of all time
SAD_subreddit = reddit.subreddit("suicidewatch+anxiety+depressed").top(limit=3000)

for post in SAD_subreddit:
    subreddit_posts.append(
        [
            post.id,
            post.author,
            post.title,
            post.score,
            post.num_comments,
            post.selftext,
            post.created,
            post.subreddit
        ]
    )

# "New" - the recent ones
SAD_subreddit = reddit.subreddit("suicidewatch+anxiety+depressed").new(limit=3000)

for post in SAD_subreddit:
    subreddit_posts.append(
        [
            post.id,
            post.author,
            post.title,
            post.score,
            post.num_comments,
            post.selftext,
            post.created,
            post.subreddit
        ]
    )

# "Hot" - currently in trending
SAD_subreddit = reddit.subreddit("suicidewatch+anxiety+depressed").hot(limit=3000)

for post in SAD_subreddit:
    subreddit_posts.append(
        [
            post.id,
            post.author,
            post.title,
            post.score,
            post.num_comments,
            post.selftext,
            post.created_utc,
            post.subreddit
        ]
    )

##Time stamp
def get_date(subreddit_posts):
	CreatedDTTM = post.created
	return datetime.datetime.fromtimestamp(CreatedDTTM)

# Transfer the scraped data into a Data Frame
SAD_subreddit_posts = pd.DataFrame(
    subreddit_posts,
    columns=[
        "ID",
        "Author",
        "Title",
        "Score",
        "Comments",
        "Post",
        "Created DTTM",
        "Post Category"
    ],
)

# DateTime format conversion
SAD_subreddit_posts["Created DTTM"] = pd.to_datetime(SAD_subreddit_posts["Created DTTM"], unit="s")

# View the Glimpse of the Dataset
SAD_subreddit_posts.head()

# Remove the Duplicates
SAD_subreddit_posts.drop_duplicates()

# Save the Data as CSV
SAD_subreddit_posts.to_csv("SAD_subreddit_Post_Data.csv")

# Download the CSV file
from google.colab import files
files.download('SAD_subreddit_Post_Data.csv')