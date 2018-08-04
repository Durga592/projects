"""cherry URL Configuration

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
################### FOR UPLOADING BEGIN HERE ####################
from django.conf.urls.static import static
from django.conf import settings
################### FOR UPLOADING ENDING HERE ####################
from ice.views import get_dashboard, get_login, user_registration, get_logout, model_form_upload, get_uploadedfiles, get_studyhall, \
api_call, api_ajax_call, model_form_order

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', get_dashboard),
    url(r'^login/', get_login),
    url(r'^registration/', user_registration),
    url(r'^logout/', get_logout),
    url(r'^uploads/form/$', model_form_upload),
    url(r'^uploadedfiles/', get_uploadedfiles),
    url(r'^studyhall/', get_studyhall),
    url(r'^apicall/', api_call),
    url(r'^apiajaxcall/', api_ajax_call),
    url(r'^order/form/$', model_form_order),
]
############################ FOR FILE UPLOADING ################################
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)