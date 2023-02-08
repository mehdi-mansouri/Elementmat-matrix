
import tweepy
import configparser
import pandas as pd

# read configs
# config = configparser.ConfigParser()
# config.read('config.ini')

# api_key = config['twitter']['api_key']
# api_key_secret = config['twitter']['api_key_secret']

# access_token = config['twitter']['access_token']
#access_token_secret = config['twitter']['access_token_secret']
api_key ='vpaJpgRsKCysnZ43jM98Wwuai'
api_key_secret='JFKhiYmCpeLzxtM1SXCRdMvJACNNdctW7NvNyZg79fKEjfu4tx'

access_token='1582440505945821195-crJLDguH6Lod0pMy37dekqsQPKEDN2'
access_token_secret='TtrflRxFDjNDsBP5rqyvVE3sLs5ZzHWWyuWyN8G3Ho1Nc'

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
# user = 'veritasium'
# limit=300

# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
keywords = '#energy'
limit=300

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)