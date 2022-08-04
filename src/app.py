import os
from secrets_manager import get_secret
import tweepy

secrets = get_secret()

def handler(event, context):
    return True