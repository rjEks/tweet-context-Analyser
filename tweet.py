
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

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" 
    
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,                  
                    'next_token': {}}
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    
    params['next_token'] = next_token 
    response = requests.request("GET", url, headers = headers, params = params)
    
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()