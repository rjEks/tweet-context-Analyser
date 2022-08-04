import os
from secrets_manager import get_secret
import tweepy
from src.tweet import set_credentials
from tweet import *
from datetime import time,  timedelta

secrets = get_secret()

def handler(event, context):
    
    ## Set twitter credentials
    bearer_token,consumer_key,consumer_secret,access_token,access_token_secret = set_credentials(secrets)
    
    ## getting client
    client = getClient(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret)
    
    ## Set common variables
    timedelta = 5
    start_time = datetime.datetime.utcnow() - timedelta
    end_time = datetime.datetime.utcnow()
    max_results = 100
    query = "#bolsonaro lang:pt"
    
    tweet_dict = searchTwitter(client, start_time.isoformat(), end_time.isoformat(), query)
    print(tweet_dict)