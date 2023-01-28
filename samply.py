import asyncio
# from base64 import encode
# from telnetlib import SE
import snscrape.modules.twitter as sntwitter
import snscrape.base
# import pandas as pd
# import numpy as np
# import json
import time
#from tw import Sentiment

from nio import AsyncClient, MatrixRoom, RoomMessageText



#--------------------Save file ----------------------------    
tweets = []


query="(#energysaving) lang:en"
#query = "(#energy) until:2023-01-27 since:2023-01-26"
for tweet in sntwitter.TwitterSearchScraper("#energysaving").get_items():
    contenttext = tweet.user.id
    print(contenttext)  
    break
