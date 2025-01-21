from dotenv import load_dotenv 
import os
import tweepy
from atproto import Client, client_utils

load_dotenv()

X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD")

x_client = tweepy.Client(
    consumer_key=X_CONSUMER_KEY,
    consumer_secret=X_CONSUMER_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_SECRET
)
response = x_client.create_tweet(text='Project posting')
print(response)







# auth = tweepy.OAuth1UserHandler(
#     consumer_key=X_CONSUMER_KEY,
#     consumer_secret=X_CONSUMER_SECRET,
#     access_token=X_ACCESS_TOKEN,
#     access_token_secret=X_ACCESS_SECRET,
# )

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
