'''The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''


from django.conf.urls import url, include
from django.contrib import admin
#from api_app import views
#from rest_framework.urlpatterns import format_suffix_patterns
#from .views import ArticlesList, Article

from api_app import views as aViews

urlpatterns = [
	url(r'^$', aViews.home, name="home"),
	url(r'^articles/$',aViews.article, name="articles_detail"),
	url(r'^articles/(?P<article_number>[0-9]+)/$', aViews.articles_detail, name = "article_view"),
    ]

#urlpatterns = format_suffix_patterns(urlpatterns)
	#^places/(?P<name>\w+)/$
