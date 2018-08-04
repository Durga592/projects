"""generic_final URL Configuration

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
from app.models import Customer, Product, Order
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', TemplateView.as_view(
    	template_name = 'app/index.html')),
    url(r'^customers/', ListView.as_view(
    	model = Customer, )),
    url(r'^createcustomer/', CreateView.as_view(
    	model = Customer,
    	success_url =	'/customers/',
    	fields =	'__all__')),
    url(r'^updatecustomer/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model = Customer,
    	success_url =	'/customers/',
    	fields =	'__all__')),
    url(r'^deletecustomer/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model = Customer,
    	template_name = 'app/customer_confirm_delete.html',
    	success_url =	'/customers/',
    	)),
    url(r'^products/', ListView.as_view(
    	model = Product,    	
    	)),
    url(r'^createproduct/', CreateView.as_view(
    	model = Product,
    	fields = '__all__',
    	success_url = '/products/'
    	)),
    url(r'^updateproduct/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model = Product,
    	fields = '__all__',
    	success_url = '/products/'
    	)),
    url(r'^deleteproduct/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model = Product,    	
    	success_url = '/products/'
    	)),
    url(r'^orders/', ListView.as_view(
    	model = Order,    	
    	)),
    url(r'^ordercreation/', CreateView.as_view(
    	model = Order,
    	fields = '__all__',
    	success_url = '/orders/'
    	)),
    url(r'^orderupdate/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model = Order,
    	fields = '__all__',
    	success_url = '/orders/'
    	)),
    url(r'^orderdelete/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model = Order,    	
    	success_url = '/orders/'
    	)),
]
