import csv
import MySQLdb
import string
from dateutil.parser import parse
import datetime
'''import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "credible_project.settings")
import django
django.setup()

from backend_app.models import InitialData'''



def populate_data():
	mydb = MySQLdb.connect(host='localhost',
		user='root',
		passwd='mysql',
		db='CredibleDB')
	cursor = mydb.cursor()
	mydb.set_character_set('utf8mb4')
	#cursor.execute("Use CredibleDB;")
	#cursor.execute("Drop table TWEET_DATA;")
	#cursor.execute("create table TWEET_DATA (article_id int PRIMARY KEY AUTO_INCREMENT, tweet_id varchar(20) NOT NULL, user_id varchar(20) NOT NULL, tweet_date datetime NOT NULL, tweet_text text NOT NULL, article_link varchar(255), title text, published_date datetime, likes int, shares int, content longtext, publisher varchar(100), topic_id int default 0, credibility_score decimal(1,1) default 0.7, UNIQUE(tweet_id, article_link));")
	#cursor.execute("ALTER TABLE TWEET_DATA AUTO_INCREMENT = 1")
	#cursor.execute("ALTER TABLE trial.TWEET_DATA MODIFY COLUMN tweet_text text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
	cursor.execute("Alter table TWEET_DATA MODIFY column credibility_score varchar(20);")


	exclude = set(string.punctuation)
	with open('tweets_csv.csv', 'r') as file:
		csv_data = csv.DictReader(file)
		#next(csv_data)
		count = 0
		for row in csv_data:
			if count == 0:
				count+=1
				continue
			try: 
				pub_dt = ""
				tweet_dt = ""
				content = ''.join(e for e in row['content'] if e.isalnum() or e == " ")
				title = ''.join(e for e in row['title'] if e.isalnum() or e == " ")
				text = ''.join(e for e in row['text'] if e.isalnum() or e == " ")
				#content = MySQLdb.escape_string(content)

				dt = parse(row['tweet_created_date'])
				tweet_dt = dt.strftime('%Y-%m-%d %H:%M:%S')

				if(str(row['pub_date']) != "nan"):
					pub_dt = datetime.datetime.strptime(row['pub_date'][:19], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

				insert_query = "INSERT INTO TWEET_DATA(tweet_id, user_id, tweet_text, article_link, shares, likes, tweet_date, title, content, published_date, publisher) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')".format(str(row['tweet_id']), str(row['user_id']), text, row['external_link'], str(row['shares']), str(row['likes']), tweet_dt, title, content, pub_dt, row['publisher'])
				print(row['tweet_id'])
				#print(insert_query)
				#cursor.execute('INSERT INTO testcsv(names, \classes, mark )' 'VALUES("%s", "%s", "%s")',  row)
				cursor.execute(insert_query)
			#close the connection to the database.
			except Exception as e:
				print("Exception", e)
				continue
			count+=1
		mydb.commit()
		cursor.close()
	return True


'''def populate_model():
	exclude = set(string.punctuation)
	with open('tweets_csv.csv', 'r') as file:
		csv_data = csv.DictReader(file)
		count = 0
		for row in csv_data:
			if count == 0:
				count += 1
				continue
			try: 
				pub_dt = ""
				tweet_dt = ""
				content = ''.join(e for e in row['content'] if e.isalnum() or e == " ")
				title = ''.join(e for e in row['title'] if e.isalnum() or e == " ")
				text = ''.join(e for e in row['text'] if e.isalnum() or e == " ")
				#content = MySQLdb.escape_string(content)

				dt = parse(row['tweet_created_date'])
				tweet_dt = dt.strftime('%Y-%m-%d %H:%M:%S')

				if(str(row['pub_date']) != "nan"):
					pub_dt = datetime.datetime.strptime(row['pub_date'][:19], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

				#tweet_data = [str(row['tweet_id']), str(row['user_id']), text, row['external_link'], str(row['shares']), str(row['likes']), tweet_dt, title, content, pub_dt, row['publisher']]
				#insert_query = "INSERT INTO TWEET_DATA(tweet_id, user_id, tweet_text, article_link, shares, likes, tweet_date, title, content, published_date, publisher) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')".format(str(row['tweet_id']), str(row['user_id']), text, row['external_link'], str(row['shares']), str(row['likes']), tweet_dt, title, content, pub_dt, row['publisher'])

				tweet_data = [str(row['tweet_id']), str(row['user_id']), text, row['external_link'], str(row['shares']), str(row['likes']), tweet_dt, title, content, pub_dt, row['publisher']]
				print(tweet_data)

				tweet_data = InitialData.objects.get_or_create(tweet_id=str(row['tweet_id']), user_id=str(row['user_id']), tweet_text=text, article_link=row['external_link'], shares=str(row['shares']), likes= str(row['likes']), tweet_date=tweet_dt, title=title, content=content, published_date=pub_dt, publisher=row['publisher'])
				tweet_data.save()
			except Exception as e:
				print("Exception: ", e)

			count += 1
		return True'''