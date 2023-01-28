import asyncio
# from base64 import encode
# from telnetlib import SE
import snscrape.modules.twitter as sntwitter 
# import pandas as pd
# import numpy as np
# import json
import time
#from tw import Sentiment

from nio import AsyncClient, MatrixRoom, RoomMessageText

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
        
        
        result = time.strftime("%I:%M %p", time.localtime())
        print(result)
        if (result=='12:50 PM'):
            query="(#energysaving) lang:en"
            #query = "(#energy) until:2023-01-27 since:2023-01-26"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():  
                contenttext = str(text_split(tweet.content))
                break
            client.login("Taghi1993!")    
            await client.room_send(
                room_id="!WJXwnykPWOjPqKlXwd:matrix.org",
                message_type="m.room.message",
                content={"msgtype": "m.text", "body":contenttext},
                )
        time.sleep(60)
asyncio.run(main())