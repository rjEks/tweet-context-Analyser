
import json
import requests
import tweepy  as tw 


def set_credentials(bearer_token,consumer_key,consumer_secret,access_token,
            access_token_secret):
#get data from vault
    return True

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