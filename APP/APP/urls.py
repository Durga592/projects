"""APP URL Configuration

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
from django.http import HttpResponse
from FIN.views import get_fin_users, empdrop, empsearch, userreg, userlogin, get_dashboard, get_logout, track_user, track_user1
'''
def get_fin_users(req):
	return HttpResponse("Welcome...")
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fin_users/', get_fin_users),
    url(r'^emp_remove/([0-9]+)/', empdrop),
	url(r'^emp_search/', empsearch),
	url(r'^user_registration/', userreg),
	url(r'^user_login/', userlogin),
    url(r'^dashboard/', get_dashboard),
    url(r'^logout/', get_logout),
    url(r'^track_user/', track_user),
    url(r'^track_user1/', track_user1),
]
