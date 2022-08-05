import boto3
import json 
from datetime import *
import uuid


def PutTweetS3(client, tweet_dict, bucket_name="twitter-context-analyser"):
    
    year=str(datetime.now().year)
    month=str(datetime.now().month)
    day=str(datetime.now().day)
    hour=str(datetime.now().hour)
    
    id = str(uuid.uuid4().hex
    tweet_name =f'tweet_{id}.json'             
    
    key = f"{year}/{month}/{day}/{hour}/{tweet_name}"
    
    for tweets in tweet_dict:
        client.put_object(Body=json.dumps(tweets), Bucket=bucket_name, key=tweet_name)
        
    return "upload complete"