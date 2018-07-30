"""Espace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import get_index_data, hall_update, hall_delete, myview, testurl

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getmyview/', myview),
    #url(r'^index/(?P<id>\d+)/(?P<type>\d+)/$', get_index_data),
    #url(r'^index/', get_index_data, kwargs={'decision': "(?P<id>d+)"}, name='group_judge_request_cut'),
    url(r'^index/(?P<title>\w+)/((?P<unique_id>\w+)/)?$', get_index_data),   #WORKING FINE...
    #url(r'^index/(?P<name>\w+)/((?P<id>\w+)/)?$', get_index_data),   #WORKING FINE...
    #url(r'^index/(?P<first_name>[a-zA-Z]+)/(?P<last_name>[a-zA-Z]+)(?:/(?P<title>[a-zA-Z]+))?/$', get_index_data),
    #url(r'^index/(?P<type>[a-zA-Z0-9]+)(?:/(?P<id>[0-9]+))?/$', get_index_data),        
    url(r'^studyhall_update/([0-9]+)/', hall_update),
    url(r'^studyhall_delete/([0-9]+)/', hall_delete),
    url(r'^get_testurl/', testurl),
]
