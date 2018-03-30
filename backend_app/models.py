from django.db import models
from django.conf import settings
from decimal import Decimal


# Create your models here.

#myFields =  ['tweet_id','user_id', 'text', 'external_link', 'shares', 'likes', 'tweet_created_date', 'title', 'content', 'author', 'pub_date']
class InitialData(models.Model):
	article_id = models.IntegerField(primary_key = True)
	tweet_id = models.CharField(max_length=20)
	user_id = models.CharField(max_length=20)
	tweet_date = models.DateField()
	tweet_text = models.TextField()
	article_link = models.URLField(null=False)
	title = models.TextField()
	published_date = models.DateField()
	content = models.TextField()
	likes = models.IntegerField(default=0)
	shares = models.IntegerField(default=0)
	publisher = models.CharField(max_length=100)
	topic_id = models.IntegerField(default = 0) #set default to self.article_id not checked yet
	credibility_score = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.7'))


	def __str__(self):
		return self.title




#class FinalData(models.Model):
	#pass


#view for the api
#class FinalView(models.Model):
	#pass