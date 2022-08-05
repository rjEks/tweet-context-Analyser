import boto3
import json 
from datetime import timedelta, datetime, timezone
from datetime import *
import datetime
import uuid


def PutTweetS3(client, tweet_dict, bucket_name="twitter-context-analyser"):
    
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    hour=str(datetime.datetime.now().hour)
    
    key = f"{year}/{month}/{day}/{hour}/"
    
    for tweets in tweet_dict:
        print(tweets)
        id = str(uuid.uuid4().hex)
        client.put_object(Body=json.dumps(tweets, default=str), Bucket=bucket_name, Key=key+id+".json")
        
    return "upload complete"