import os
from src.secrets_manager import get_secret
from tweepy import *
from src.tweet import set_credentials
from src.tweet import *
from datetime import time,  timedelta
import datetime
from src.comprehend import *
import boto3

secrets = get_secret()

client_comprehend = boto3.client('comprehend')

def handler(event, context):
    
    ## Set twitter credentials
    bearer_token,api_key,api_key_secret,access_token,\
    access_token_secret = set_credentials(secrets)
    
    ## getting client
    client = getClient(bearer_token,api_key,api_key_secret,access_token, \
                       access_token_secret)
   
    
    ## Set common variables
    timedelta_days = timedelta(5)
    timedelta_days_between = timedelta(1)
    start_time = datetime.datetime.now(datetime.timezone.utc) - timedelta_days
    end_time = datetime.datetime.now(datetime.timezone.utc) - timedelta_days_between
    max_results = 20
    query = "bolsonaro lang:pt"   
    
    ## search twitter 
    tweet_dict = searchTwitter(client, start_time.isoformat(), \
                               end_time.isoformat(), max_results, query)
    
    ## using comprehend
    tweet_sentiment_analysis_dict = detectSentiment(client_comprehend,tweet_dict,query)
    print(tweet_sentiment_analysis_dict)
    
    
