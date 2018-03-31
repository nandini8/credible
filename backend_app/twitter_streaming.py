#Import the necessary methods from tweepy library
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import time
import workerpool
from tweepy.streaming import StreamListener
from backend_app.process_tweets import DownloadJob
from datetime import datetime, timedelta
from backend_app.trending_tags import extractTrendingTags
from backend_app.populate_initialdata import populate_data
from backend_app.allocate_topicid_credibility import populate_update_data


#import pandas as pd
#import json
#import threading
#tweets_data_path = 'fetched_tweets.json'
#tweets_csv_data_path = 'tweets_csv.csv'
#myFields =  ['tweet_id','user_id', 'text', 'external_link', 'link', 'shares', 'likes', 'tweet_created_date']
#count = 0

access_token = '941534431646330881-swNBwYQsuPZP4yd3UMo0gNXIyyENO0f'
access_token_secret = '2mMoFY3HzeWerXNIaGl6f4VMCLoSSsAgTJZAZjLuAMk6Z'
consumer_key = 'bxHiTcKEDH0Drr6ntpKnlA2FV'
consumer_secret = '2QOs9ux6gMt0FSIEfs4OqLWGHwAhhg3VX84oEpSgRlg0x6rVbh'
        
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.pool = workerpool.WorkerPool(size=30)
        super(StdOutListener, self).__init__()
        
    def on_status(self, status):
        if status.retweeted or status.lang != "en":
            return
        
#        print(status.author.time_zone)
        
        if (time.time() - self.start_time) < self.limit: 
            job = DownloadJob(status)
            self.pool.put(job)
            return True
        else:
            self.pool.shutdown()
            self.pool.wait()
            return False

    def on_error(self, status):
        print(status)



#if __name__ == '__main__':
def run_streaming():
    #This handles Twitter authetification and the connection to Twitter Streaming API

    l = StdOutListener(time_limit=30)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')
    
    api = API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078])
    stream.filter(track=extractTrendingTags(), languages=["en"])
    print("Streaming complete. Creating initial database")

    value = populate_data()
    print("populated data", value)

    populate_update_data()
    print("END")




