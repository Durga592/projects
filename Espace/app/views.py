# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Ehall, Eexpenses, Eenquiry
# Create your views here.
def get_index_data(request):
	get_hall	=	Ehall.objects.all()
	get_expense	=	Eexpenses.objects.all()
	get_enquiry	=	Eenquiry.objects.all()
	return render(request, "app/index.html", {"data":get_hall, "expense_data":get_expense, "enquiry_data":get_enquiry})