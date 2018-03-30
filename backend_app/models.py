from django.db import models
from django.conf import settings


# Create your models here.

#myFields =  ['tweet_id','user_id', 'text', 'external_link', 'shares', 'likes', 'tweet_created_date', 'title', 'content', 'author', 'pub_date']
class InitialData(models.Model):
	tweet_id = models.CharField(max_length=20)
	user_id = models.CharField(max_length=20)
	tweet_created_date = models.DateField()
	published_date = models.DateField()
	tweet_text = models.TextField()
	external_link = models.URLField(null=False)
	title = models.TextField()
	author = models.CharField(max_length=50)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	shares = models.IntegerField(default=0)
	#credibility_score = models.IntegerField(default=7)


	def __str__(self):
		return self.title




#class FinalData(models.Model):
	#pass


#view for the api
#class FinalView(models.Model):
	#pass