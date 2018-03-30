from django.shortcuts import render
from backend_app import twitter_streaming
from django.http import HttpResponse

# Create your views here.

def populate_init_data(request):
	twitter_streaming.run_streaming()
	return HttpResponse("Data done!")

