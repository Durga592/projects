# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pagi_app.models import Contacts
############### FOR PAGINATION ##########################################
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.

def listing(request):
	contact_list = Contacts.objects.all()
	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'pagi_app/list.html', {'contacts': contacts})

def listing_new(request):
	current_page = int(request.GET.get('page' ,'1'))
	getlimit = 25 * current_page
	offset = int(getlimit) - 25
	contact_list = Contacts.objects.all()[offset:getlimit]  # limiting contacts based on current_page
	total_contacts = Contacts.objects.all().count()  
	total_pages = total_contacts / 25
	if total_contacts % 25 != 0:
	    total_pages += 1 # adding one more page if the last page will contains less contacts 
	    pagination = make_pagination_html(current_page, total_pages)
	return render(request, 'pagi_app/list.html', {'contacts': contact_list, 'pagination': pagination})

def make_pagination_html(current_page, total_pages):
	pagination_string = ""
	if current_page > 1:
		pagination_string += '<a href="?page=%s">previous</a>' % (current_page -1)
	pagination_string += '<span class="current"> Page %s of %s </span>' %(current_page, total_pages)
	if current_page < total_pages:
		pagination_string += '<a href="?page=%s">next</a>' % (current_page + 1)
	return pagination_string