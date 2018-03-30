from django.shortcuts import render
from django.http import HttpResponse
'''from rest_framework import generics, status
from .serializers import INITIALTABLESerializer
from .serializers import FINALTABLESerializer
from .models import INITIALTABLE'''
import MySQLdb
import json
import datetime


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def home(request):
	return HttpResponse("Options available in the api")


def article(request):
	mydb = MySQLdb.connect(host='localhost',
		user='root',
		passwd='mysql',
		db='CredibleDB')
	cursor = mydb.cursor()
	mydb.set_character_set('utf8mb4')
	query = 'SELECT article_id, title, content, credibility_score, publisher, published_date, article_link FROM TWEET_DATA;'
	cursor.execute(query)
	article_details = cursor.fetchall()
	articles = []
	for row in article_details:
		d = dict()
		d['article_id'] = row[0]
		d['title'] = row[1]
		d['content'] = row[2]
		d['credibility_score'] = str(row[3])
		d['publisher'] = row[4]
		d['published_date'] = row[5]
		d['article_link'] = row[6]
		articles.append(d)
	j = json.dumps(articles, default = myconverter)
	cursor.close()
	return HttpResponse(j)


def articles_detail(request, article_number):

	print(article_number)
	mydb = MySQLdb.connect(host='localhost',
		user='root',
		passwd='mysql',
		db='CredibleDB')
	cursor = mydb.cursor()
	mydb.set_character_set('utf8mb4')
	query = 'SELECT article_id, title, content, publisher, published_date, credibility_score, article_link FROM TWEET_DATA WHERE article_id = ' + article_number + ';'
	print(query)
	print("Article number", article_number)
	cursor.execute(query)
	article = cursor.fetchall()
	articles = []
	for row in article:
		d = dict()
		d['article_id'] = row[0]
		d['title'] = row[1]
		d['content'] = row[2]
		d['publisher'] = row[3]
		d['published_date'] = row[4]
		d['credibility_score'] = str(row[5])
		d['article_link'] = row[6]
		articles.append(d)
	j = json.dumps(articles, default = myconverter)
	cursor.close()
	return HttpResponse(j)	