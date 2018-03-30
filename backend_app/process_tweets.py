import workerpool
import json
from urllib.request import urlopen
from urllib.parse import urlparse
import pandas as pd
import threading
import re
import newspaper
import traceback
import csv
import tldextract
import http.client
from backend_app.date_extractor import extractArticlePublishedDate


tweets_data_path = 'fetched_tweets.json'
tweets_csv_data_path = 'tweets_csv.csv'
myFields =  ['tweet_id','user_id', 'text', 'external_link', 'shares', 'likes', 'tweet_created_date', 'title', 'content', 'pub_date', 'publisher']
count = 0
with open(tweets_csv_data_path, 'w') as file:
	writer = csv.DictWriter(file, fieldnames=myFields)
	writer.writeheader()


class Article():
	
	def _init_(self, title, content, pub_date, publisher):
		self.title = title
		self.content = content
		self.pub_date = pub_date  
		self.publisher = publisher
	

class DownloadJob(workerpool.Job):
	"Job for downloading a given URL."
	def __init__(self, status):
		self.status = status # The url we'll need to download when the job runs
	
	def is_social_url(self, myurl):
		social_words = ['youtube.com', 'instagram.com', 'twitter.com', 'facebook.com', 'youtu.be']
		
		for word in social_words:
			if word in myurl:
				return True
		return False
	
	def fetch_article(self, myurl):
		try:
			first_article = newspaper.Article(url=myurl)
			first_article.download()
			first_article.parse()
			title = first_article.title
			if not title:
				return None
			pub_date = extractArticlePublishedDate(myurl)
			if not pub_date:
				return None
			content = first_article.text
			if not content:
				return None

			fp = urlopen(myurl)
			full_url = fp.geturl()
			publisher = tldextract.extract(full_url).domain + '.' + tldextract.extract(full_url).suffix

			article_obj = Article()
			article_obj.title = title.replace(';', '')
			article_obj.content = content.replace(';', '')
			article_obj.pub_date = pub_date
			article_obj.publisher = publisher
			return article_obj

		except Exception as e:
			print("Exception", e)
			return None
	
	def parse_tweet(self, tweet): #tweet parameter is a JSON 
	
		try:
			with open(tweets_csv_data_path, 'a') as file:
				writer = csv.writer(file)
				finalList = []
				

				#Extract the original tweet too!!!
				if 'quoted_status' in tweet and 'extended_tweet' in tweet['quoted_status']:
					
					for each_value in tweet['quoted_status']['extended_tweet']['entities']['urls']:
						my_url = each_value['expanded_url']

						print("Quoted Tweet: by ", tweet['quoted_status']['user']['id_str'], my_url)

						article_obj = self.fetch_article(my_url)
						if article_obj:
							if self.is_social_url(article_obj.publisher):
								continue
							json_record = self.status._json
							print(json_record['quoted_status']['id_str'])
							finalList = [str(json_record['quoted_status']['id_str']), str(json_record['quoted_status']['user']['id_str']), json_record['quoted_status']['extended_tweet']['full_text'].replace(';', ''),my_url, json_record['quoted_status']['retweet_count'], json_record['quoted_status']['favorite_count'], json_record['quoted_status']['created_at'], article_obj.title, article_obj.content, article_obj.pub_date, article_obj.publisher]
							writer.writerow(finalList)

						
				if 'extended_tweet' in tweet and len(tweet['extended_tweet']['entities']['urls']) > 0:	
					for each_value in tweet['extended_tweet']['entities']['urls']:
						my_url = each_value['expanded_url']

						print("Extended Tweet: by ", tweet['user']['id_str'], my_url)    
						article_obj = self.fetch_article(my_url)
						if article_obj:
							if self.is_social_url(article_obj.publisher):
								continue
							json_record = self.status._json
							print(json_record['id_str'])
							finalList = [str(json_record['id_str']), str(json_record['user']['id_str']), json_record['extended_tweet']['full_text'].replace(';', '') ,my_url, json_record['retweet_count'], json_record['favorite_count'], json_record['created_at'], article_obj.title, article_obj.content, article_obj.pub_date, article_obj.publisher]
							writer.writerow(finalList)

					
				elif 'entities' in tweet and len(tweet['entities']['urls']) > 0:   
					 
					for each_value in tweet['entities']['urls']:
						
						my_url = each_value['expanded_url']
						
						print("Tweet: by ", tweet['user']['id_str'], my_url)  
						article_obj = self.fetch_article(my_url)
						if article_obj:
							if self.is_social_url(article_obj.publisher):
								continue
							json_record = self.status._json
							print(json_record['id_str'])
							finalList = [str(json_record['id_str']), str(json_record['user']['id_str']), json_record['text'].replace(';', ''),my_url, json_record['retweet_count'], json_record['favorite_count'], json_record['created_at'], article_obj.title, article_obj.content, article_obj.pub_date, article_obj.publisher]
							writer.writerow(finalList)
			
		except Exception as e:
			traceback.print_exc()

	def run(self):
		tweet = self.status._json
		self.parse_tweet(tweet)
		
		