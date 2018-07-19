# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Ehall, Eexpenses, Eenquiry, Ecourse, Estudent
# Create your views here.
def get_index_data(request):	
	print request.method
	hall_msg 	=	''
	enquiry_msg	=	''
	expense_msg	=	''
	course_msg	=	''
	student_msg	=	''
	if request.method == "POST":
		print request.POST
		########## CONDITION FOR STUDYHALL FORM ######################
		if request.POST['tab_type'] == 'type_study_hall':
			#import pdb
			#pdb.set_trace()
			hall_instance	=	Ehall(name = request.POST['h_name'], 
										area = request.POST['h_area']
									)
			hall_instance.save()		
			hall_msg		=	'Successfully Study Hall data Created'
		########## CONDITION FOR ENQUIRY FORM ######################
		if request.POST['tab_type']	==	'type_enquiry':
			course_instance		=	Ecourse.objects.get(id = request.POST['e_course'])
			student_instance	=	Estudent.objects.get(id = request.POST['e_student'])
			#print request.course_instance.POST['e_course']
			e_instance		=	Eenquiry(name = request.POST['e_enquiry'], 
											course = course_instance, 
											student = student_instance
										)
			e_instance.save()
			enquiry_msg		=	'Successfully Enquiry form data inserted'
		########## CONDITION FOR EXPENSES FORM ######################
		if request.POST['tab_type']	==	'type_expenses':
			e_hall_instance 	=	Ehall.objects.get(id = request.POST['ex_hall'])
			expense_instance	=	Eexpenses(ehall = e_hall_instance, 
												date = request.POST['ex_date'], 
												name = request.POST['ex_name'], 
												dec = request.POST['ex_desc'], 
												value = request.POST['ex_value']
											)
			expense_instance.save()
			expense_msg			=	'Successfully expenses data inserted'
		########## CONDITION FOR COURSE FORM ########################
		if request.POST['tab_type']	==	'type_course':
			get_course_instance	=	Ecourse(name = request.POST['c_name'])
			get_course_instance.save()
			course_msg			=	'Successfully course created'
		########## CONDITION FOR STUDENT FORM #######################
		if request.POST['tab_type']	==	'type_student':
			get_student_instance	=	Estudent(name = request.POST['s_name'], 
													address = request.POST['s_addrs'], 
													phone = request.POST['s_phone'], 
													email = request.POST['s_email']
												)
			get_student_instance.save()
			student_msg				=	'Successfully student created'

	get_hall	=	Ehall.objects.all()
	get_expense	=	Eexpenses.objects.all()
	get_enquiry	=	Eenquiry.objects.all()
	get_course	=	Ecourse.objects.all()
	get_student	=	Estudent.objects.all()
	return render(request, "app/index.html", {"data":get_hall, 
												"hall_suc_msg":hall_msg, 
												"expense_data":get_expense, 
												"enquiry_data":get_enquiry,
												"course_data":get_course,
												"student_data":get_student,
												"enquiry_suc_msg":enquiry_msg,
												"expense_suc_msg":expense_msg,
												"course_suc_msg":course_msg,
												"student_suc_msg":student_msg
											}
				)