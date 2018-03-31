import MySQLdb
import pandas as pd
#from similar_article import getArticleTopicIds
#from backend_app.predict_on_stemmed_data import credibility
#from backend_app.update_script import update

def populate_update_data():
	mydb = MySQLdb.connect(host='localhost',
		user='root',
		passwd='mysql',
		db='CredibleDB')
	cursor = mydb.cursor()
	mydb.set_character_set('utf8mb4')

	select_query = "select article_id, content from TWEET_DATA;"
	#select_query_2 = "select tweet_id from TWEET_DATA;"

	'''cursor.execute(select_query)
	select_object = cursor.fetchall()

	cursor.execute(select_query_2)
	select_tweet_id = cursor.fetchall()
	list_of_ids = []
	for tweet in select_tweet_id:
		for t in tweet:
			list_of_ids.append(t)
	df = pd.DataFrame(data={'tweet_id': list_of_ids})
	df.index.name = 'row_id'
	df = update(df)
	print(df)
	for ind in df.index:
		update_query = "update TWEET_DATA set likes = likes + " + str(df.loc[ind, 'likes']) + " ,shares =  shares + " + str(df.loc[ind, 'shares']) + " where tweet_id = " +str(df.loc[ind, 'tweet_id']) + ";"
		print(update_query)
		cursor.execute(update_query)
	mydb.commit()'''



	

	article_dict = []
	for obj in select_object:
		article_dict.append({'article_id': obj[0], 'content': obj[1]})

	df = pd.DataFrame(article_dict)
	df.index.name = 'row_id'
	df = credibility(df,'content')
	print(df)
	for ind in df.index:
		#print(df.loc[ind, 'topics_id'])
		set_query = "update TWEET_DATA set credibility_score = " + str(df.loc[ind, 'credibility_score']) + " where article_id = " + str(df.loc[ind, 'article_id']) + ";"
		print(set_query)
		cursor.execute(set_query)
	mydb.commit()
	
	'''df = getArticleTopicIds(df)
	for ind in df.index:
		#print(df.loc[ind, 'topics_id'])
		set_query = "update TWEET_DATA set topic_id = " + str(df.loc[ind, 'topics_id']) + " where article_id = " + str(df.loc[ind, 'article_id']) + ";"
		print(set_query)
		cursor.execute(set_query)
	mydb.commit()'''	

	cursor.close()

	#df = pd.DataFrame(article_dict)
	#df.index.name = 'row_id'
