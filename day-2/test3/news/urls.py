"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from .views import news,news_data,get_post,data
urlpatterns = [
    url(r'^$',news,name='news'),
    url(r'^(\d+)/(\d+)/(\d+)/$',news_data,name='news_data'),
	url(r'^get_post/$',get_post,name='get_post'),
	url(r"^data",data,name='data'),

]
