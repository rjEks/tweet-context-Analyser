
import json
import requests
import tweepy  as tw 
import os
import re

def set_credentials(bearer_token,consumer_key,consumer_secret,access_token,
            access_token_secret):

    bearer_token=os.environ['BEARER_TOKEN']
    consumer_key=os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    
    return bearer_token,consumer_key,consumer_secret,access_token,access_token_secret
    

def getClient(bearer_token,consumer_key,consumer_secret,access_token,
            access_token_secret):    

    client = tw.Client(bearer_token=bearer_token, 
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret )
    return client

def searchTwitter(client, start_time, end_time, max_results=10, query="#bolsonaro lang:pt"):
    
    tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = max_results,
                                     expansions='author_id'
                                     )
    tweets_dict = [dict(tweets_no_format) for tweets_no_format in tweets.data]
    return tweets_dict

def cleanTweet(tweets_dict):
    
    for tweets in tweets_dict:
        tweets["text"] = re.sub(r"(@[A-Za-z0–9_]+)|[^\w\s]|#|http\S+", "", tweets["text"])
    
    return tweets_dict