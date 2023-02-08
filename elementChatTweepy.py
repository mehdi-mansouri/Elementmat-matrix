import asyncio
# from base64 import encode
# from telnetlib import SE
import snscrape.modules.twitter as sntwitter 
# import pandas as pd
# import numpy as np
# import json
import tweepy
import time
#from tw import Sentiment

from nio import AsyncClient, MatrixRoom, RoomMessageText

api_key ='vpaJpgRsKCysnZ43jM98Wwuai'
api_key_secret='JFKhiYmCpeLzxtM1SXCRdMvJACNNdctW7NvNyZg79fKEjfu4tx'

access_token='1582440505945821195-crJLDguH6Lod0pMy37dekqsQPKEDN2'
access_token_secret='TtrflRxFDjNDsBP5rqyvVE3sLs5ZzHWWyuWyN8G3Ho1Nc'
#Authentication
auth = tweepy.OAuthHandler(api_key ,api_key_secret)
auth.set_access_token(access_token ,access_token_secret)
api = tweepy.API(auth)
def text_split(tweet):
    # precprcess tweet
    tweet_words = []
    for word in tweet.split(' '):
        if len(word.split('\n')) >1:
            for words in word.split('\n'):
                if words.startswith('http'):
                    words = ""
                elif words.startswith('#'):
                    words = ""
                elif word.startswith('@') and len(word) > 1:
                    words = '@user'
                tweet_words.append(words)
        elif word.startswith('@') and len(word) > 1:       
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        elif word.startswith(r"\ud"):
            word = ""
        elif word.startswith('#'):           
            word = ""

        elif len(word.split('\n')) ==1:
            tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)
    return tweet_proc

#--------------------Save file ----------------------------    
tweets = []
text_keywords=[]
posetive_tweets=[]
negative_tweets=[]
neutral_tweets=[]
limit =2

   
async def main():
    client = AsyncClient("https://matrix.org", "mehdimansouri1")
    response = await client.login("Taghi1993!")
    print(response)
    while (True):
        sync_response = await client.sync(380)
        print(sync_response) # note that this could be LARGE!
        keywords='#energy lang:en'
        limit =20
        tweets=tweepy.Cursor(api.search_tweets,q=keywords,
            count=100,tweet_mode='extended').items(limit)
        result = time.strftime("%I %p", time.localtime())
        print(result)
        if (result=='08 PM'):
            for tweet in tweets:
                print(1)
                contenttext = str(text_split(tweet.full_text))
                print(contenttext)
                break;
            await client.login("Taghi1993!")    
            await client.room_send(
                room_id="!WJXwnykPWOjPqKlXwd:matrix.org",
                message_type="m.room.message",
                content={"msgtype": "m.text", "body":contenttext},
                )
        time.sleep(60)
asyncio.run(main())