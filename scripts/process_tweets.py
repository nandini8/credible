import workerpool
import json
import pandas as pd
import threading


tweets_data_path = 'fetched_tweets.json'
tweets_csv_data_path = 'tweets_csv.csv'
myFields =  ['tweet_id','user_id', 'text', 'external_link', 'link', 'shares', 'likes', 'tweet_created_date']
count = 0

class DownloadJob(workerpool.Job):
    "Job for downloading a given URL."
    def __init__(self, status):
        self.status = status # The url we'll need to download when the job runs
    
    def run(self):
        
        try:
            tweet = self.status._json
            if tweet['place']['country_code'] == 'IN':
                
                print(json.dumps(self.status._json))
        
                with open(tweets_data_path,'a') as tf:
                    tf.write(json.dumps(self.status._json)+"\n")
                        
                finalList = []
                if(tweet['entities']['urls']):
                    for each_value in tweet['entities']['urls']:
                        #for value1 in tweet['extended_tweet']['entities']['urls']:
                        #for value2 in tweet['entities']['urls']:
                        newList = [str(tweet['id_str']), 
                        str(tweet['user']['id_str']), 
                        self.status.text.replace(';',''), 
                        each_value['expanded_url'],
                        list(value['expanded_url'] for value in tweet['entities']['urls']) , 
                        tweet['retweet_count'], 
                        tweet['favorite_count'], 
                        tweet['created_at']]
                        
                        #list(value['expanded_url'] for value in tweet['extended_tweet']['entities']['urls']), list(value['expanded_url'] for value in tweet['entities']['urls'])
                        finalList.append({myFields[i]:newList[i] for i in range(len(myFields))})
                    
                    df = pd.DataFrame(finalList)
                    df.index.name = 'row_id'
                    csv_output_lock = threading.Lock()
                    with csv_output_lock:
                        df.to_csv(tweets_csv_data_path, mode='a')
        
        except Exception as e:
            print(e)
