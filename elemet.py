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
inc=0

async def message_callback(room: MatrixRoom, event: RoomMessageText) -> None:
    print(
        f"Message received in room {room.display_name}\n"
        f"{room.user_name(event.sender)} | {event.body}"
    )
    
    result = time.strftime("%I:%M:%S %p", time.localtime())
    print(result)
    #if(result=='01:06:00 PM' or result=='01:07:00 PM' or result=='01:08:00 PM'):
    client = AsyncClient("https://matrix.org", "mehdimansouri1")
    #client = AsyncClient("https://matrix.org", "USER_NAME")
    print(await client.login("Taghi1993!"))
    #qeuery=sntwitter.TwitterSearchScraper(query).get_items()
    query="(#energytips) lang:en"
    time.sleep(20)  
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        #content_sentiment = Sentiment.sentiment_scores(tweet.content)    
        contenttext = str(text_split(tweet.content))
        print(contenttext)
        inc+=1
        print(inc)
        break   
    await client.room_send(
        room_id="!WJXwnykPWOjPqKlXwd:matrix.org",
        message_type="m.room.message",
        content={"msgtype": "m.text", "body":contenttext},
    )
async def main() -> None:
    # client = AsyncClient("https://matrix.example.org", "@alice:example.org")
    # client.add_event_callback(message_callback, RoomMessageText)

    # print(await client.login("my-secret-password"))

    client = AsyncClient("https://matrix.org", "mehdimansouri1")
    client.add_event_callback(message_callback, RoomMessageText)
    print(await client.login("Taghi1993!"))
    # "Logged in as @alice:example.org device id: RANDOMDID"

    # If you made a new room and haven't joined as that user, you can use
    # await client.join("your-room-id")

    # await client.room_send(
    #     # Watch out! If you join an old room you'll see lots of old messages
    #     room_id="!my-fave-room:example.org",
    #     message_type="m.room.message",
    #     content={"msgtype": "m.text", "body": "Hello world!"},
    # )
    await client.sync_forever(timeout=30000)  # milliseconds

asyncio.run(main())