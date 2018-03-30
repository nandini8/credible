from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
	return render(request, 'index.html')

def newsView(request):
	return render(request, 'newsview.html')

def about(request):
	return render(request, 'about.html')

def features(request):
	return render(request, 'features.html')
