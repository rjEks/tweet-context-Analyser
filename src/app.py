import os
from src.secrets_manager import get_secret
from tweepy import *
from src.tweet import set_credentials
from src.tweet import *
from datetime import timedelta, datetime, timezone
import datetime
from src.comprehend import *
import boto3
from src.s3 import *
import ast

secrets = get_secret()

client_comprehend = boto3.client('comprehend')
client_s3 = boto3.client("s3")
dynamodb_client = boto3.resource("dynamodb")

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
    max_results = 50
    query = "bolsonaro -is:retweet lang:pt"
    
    ## search twitter 
    tweet_dict = searchTwitter(client, start_time.isoformat(), \
                               end_time.isoformat(), max_results, query)
    
    ## using comprehend
    tweet_sentiment_analysis_dict = detectSentiment(client_comprehend,tweet_dict
                                                    ,query)
    
    ## Clean Tweets
    tweet_sentiment_cleaned_dict = cleanTweet(tweet_sentiment_analysis_dict)
    json_tweet_sentiment_cleaned_dict = json.dumps(tweet_sentiment_cleaned_dict,
                                                   default=str)
    
    #put in dynamo db
    tweet_file_reader = ast.literal_eval(json_tweet_sentiment_cleaned_dict)
    tweet_table = dynamodb_client.Table('Tweets')
    for item in tweet_file_reader:
        tweet_table.put_item(Item=item)
    
    ## Put in S3 -TODO Refactor
    tweet_dict_s3 = searchTwitter(client, start_time.isoformat(), \
                               end_time.isoformat(), max_results, query)
                               
    tweet_sentiment_analysis_dict_s3 = detectSentiment(client_comprehend,
                                                     tweet_dict_s3
                                                    ,query)
                                                    
    tweet_sentiment_cleaned_dict_s3 = cleanTweet(
                                                tweet_sentiment_analysis_dict_s3)
     
    PutTweetS3(client_s3,tweet_sentiment_cleaned_dict_s3)
    
    
    
    
