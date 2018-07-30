# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.http import HttpResponseRedirect
#HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import Ehall, Eexpenses, Eenquiry, Ecourse, Estudent
# Create your views here.
def myview(request):
    return  HttpResponseRedirect(reverse('get_index_data', args=[1945]))
################ALL TABS DATA INSERTION BEGIN HERE###############################################
def get_index_data(request, title= '', *args, **kwargs):	
	#print request.method
	print '################## 1) DEBUGGING BEGIN HERE ####################'
	print request
	print title	
	print type(args), args
	print type(kwargs), kwargs, kwargs['unique_id']
	print '################## 1) DEBUGGING ENDING HERE ####################'
	print '<br>'
	hall_msg 	=	''
	enquiry_msg	=	''
	expense_msg	=	''
	course_msg	=	''
	student_msg	=	''
	edit_hall_data	=	''
	edit_Eexpenses_data	=	''
	#################### POST METHOD ############################################################
	if request.method == "POST":
		#print request.POST
		########## CONDITION FOR STUDYHALL FORM ######################
		if request.POST['tab_type'] == 'type_study_hall':
			#import pdb
			#pdb.set_trace()
			if kwargs['unique_id'] > 0:				
				edit_hall_data				=	Ehall.objects.get(id = kwargs['unique_id'])
				edit_hall_data.name 			=	request.POST['h_name']
				edit_hall_data.area 			=	request.POST['h_area']
				edit_hall_data.hall_status 	=	request.POST['e_status']
				edit_hall_data.save()
				hall_msg		=	'Successfully Study Hall data updated'				
			else:
				hall_instance	=	Ehall(name = request.POST['h_name'], 
											area = request.POST['h_area']
										)
				hall_instance.save()		
				hall_msg		=	'Successfully Study Hall data inserted'
		########## CONDITION FOR ENQUIRY FORM ######################
		if request.POST['tab_type']	==	'type_enquiry':
			course_instance		=	Ecourse.objects.get(id = request.POST['e_course'])
			student_instance	=	Estudent.objects.get(id = request.POST['e_student'])
			if kwargs['unique_id'] > 0:
				edit_Eexpenses_data				=	Eenquiry.objects.get(id = kwargs['unique_id'])
				edit_Eexpenses_data.name 		=	request.POST['e_enquiry']
				edit_Eexpenses_data.course_id 	=	course_instance
				edit_Eexpenses_data.student_id 	=	student_instance
				edit_Eexpenses_data.enquiry_status	=	request.POST['en_status']
				edit_Eexpenses_data.save()
				enquiry_msg		=	'Successfully Enquiry form data updated'				
			else:
				#course_instance		=	Ecourse.objects.get(id = request.POST['e_course'])
				#student_instance	=	Estudent.objects.get(id = request.POST['e_student'])				
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
	print '################## 2) DEBUGGING BEGIN HERE ####################'
	print request
	print title	
	print type(args), args
	print type(kwargs), kwargs, kwargs['unique_id']
	print '################## 2) DEBUGGING ENDING HERE ####################'
	######################GET METHOD#############################################################	
	if request.method == 'GET':		
		if kwargs['unique_id'] > 0 and title == 'hall':
			edit_hall_data	=	Ehall.objects.get(id = kwargs['unique_id'])
		if kwargs['unique_id'] > 0 and title == 'enquiry':
			edit_Eexpenses_data	=	Eexpenses.objects.get(id = kwargs['unique_id'])
		if kwargs['unique_id'] > 0 and title == 'expenses':
			pass
		if kwargs['unique_id'] > 0 and title == 'courses':
			passs
		if kwargs['unique_id'] > 0 and title == 'students':
			pass
		pass
	print edit_hall_data
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
												"student_suc_msg":student_msg,
												"get_edit_hall_data":edit_hall_data,
												"get_edit_Eexpenses_data":edit_Eexpenses_data,
											}
				)
######################ALL TABS DATA INSERTION ENDING HERE##############################################################
######################STUDY HALL OPERATIONS BEGIN HERE##############################################################
def hall_update(request, hallid):
	e_hall_instance 	=	Ehall.objects.get(id = hallid)
	return render(request, "app/hall_update")

def hall_delete(request, hallid):
	e_hall_instance 	=	Ehall.objects.get(id = hallid)
	e_hall_instance.delete()
	suc_msg 			=	'Successfully hall deleted'
	hall_data			=	Ehall.objects.all()
	return redirect('/index/')
######################STUDY HALL OPERATIONS ENDING HERE##############################################################
def testurl(request):
	return render(request, "app/test.html")