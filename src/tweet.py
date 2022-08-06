
import json
import requests
import tweepy  as tw 
import os
import re

def set_credentials(secrets):

    bearer_token=secrets['BEARER_TOKEN']
    access_token = secrets['ACCESS_TOKEN']
    access_token_secret = secrets['ACCESS_TOKEN_SECRET']
    api_key = secrets['API_KEY']
    api_key_secret = secrets['API_KEY_SECRET']
    
    return bearer_token,api_key,api_key_secret,access_token,access_token_secret
    

def getClient(bearer_token,api_key,api_key_secret,access_token,
            access_token_secret):    

    client = tw.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_key_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret )
    return client

def searchTwitter(client, start_time, end_time, max_results=10, query="bolsonaro lang:pt"):
    
    tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["created_at", "text", 
                                                     "source"],
                                     user_fields = ["name", "username", 
                                                    "location", "verified", 
                                                    "description"],
                                     max_results = max_results,
                                     expansions='author_id'
                                     )
    tweets_dict = [dict(tweets_no_format) for tweets_no_format in tweets.data]
    return tweets_dict

def cleanTweet(tweets_dict):
    
    for tweets in tweets_dict:
        #remove mentions
        tweets["text"] = re.sub("@[A-Za-z0-9_]+", "", tweets["text"])
        #remove hastags
        tweets["text"] = re.sub("#[A-Za-z0-9_]+", "", tweets["text"])
        #remove http
        tweets["text"] = re.sub(r"https\S+", "", tweets["text"])
        #remove links
        tweets["text"] = re.sub(r"www.\S+", "", tweets["text"])
    
    return tweets_dict