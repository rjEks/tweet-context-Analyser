import os
import boto3


def detectSentiment(client, Text, LanguageCode="pt"):
    
    sentiment = client.detect_sentiment(Text=Text, LanguageCode=LanguageCode)
    response_sentiment = sentiment['Sentiment']
    
    
    return response_sentiment

def detectEntities(client, Text, LanguageCode="pt"):
    
    entities = client.detect_entities(Text = Text, LanguageCode = LanguageCode)
    entities = entities['Entities']
    
    textEntities = [dict_item['Text'] for dict_item in entities] 
    typeEntities = [dict_item['Type'] for dict_item in entities] 
    
    return textEntities, typeEntities
   
    
    
    
    