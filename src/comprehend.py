def DetectSentiment(client, tweet_dict, arg_query, LanguageCode="pt"):

    for tweets in tweet_dict:
        sentiment = client.detect_sentiment(Text=tweets["text"],
                                            LanguageCode=LanguageCode)
        tweets["sentiment"] = sentiment['Sentiment']
        tweets["query"] = arg_query

    return tweet_dict


def DetectEntities(client, Text, LanguageCode="pt"):

    entities = client.detect_entities(Text=Text, LanguageCode=LanguageCode)
    entities = entities['Entities']

    textEntities = [dict_item['Text'] for dict_item in entities]
    typeEntities = [dict_item['Type'] for dict_item in entities]

    return textEntities, typeEntities
