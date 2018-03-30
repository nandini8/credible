from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
	return HttpResponse("Options available in the api")

def article(request):
	return HttpResponse("Json data displayed here")