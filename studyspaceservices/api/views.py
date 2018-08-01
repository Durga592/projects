# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ExpSerializer, StudentSerailizer, ExpensesSerializer, EnqurySerializer
from api.models import Ehall, Estudent, Ecourse, Eenquiry, Eexpenses, New
import datetime
# Create your views here.
class StudyHallView(APIView):
	def post(self, request):
		try:
			sh = Ehall(**request.data)
			sh.save()
			return Response("welcome")
		except Exception as err:
			return Response(err.message)
	def get(self, request):
		return Response("Hello welcome")
	def put(self, request):
		return Response("Hello welcome")

class EhallDetailView(APIView):
	def post (self, request, id):
		#import pdb; pdb.set_trace()
		try:
			hall = Ehall.objects.get(pk = id)
			data = request.data
			hall.name = data.get("name", hall.name)
			hall.area = data.get("area", hall.area)
			hall.save()
			return Response("Updated successfully")
		except Exception as err:
			return Response(err.message)
############## AJAX CALLING ######################################################################
############## FOR STUDY HALL OPERATIONS ##########################################################
class EhallView(APIView):
	def post(self, request):
		try:
			print request.data
			print 'BEGIN 111111111111111111111111111111111..........'
			print request.data.get('name')
			print request.data.get('area')
			print 'BEGIN 111111111111111111111111111111111..........'
			hall_data	=	Ehall(**request.data)
			hall_data.save()
			return Response("Hall successfully created...", status.HTTP_201_CREATED)
		except Exception as exp:
			return Response(exp.message, status.HTTP_400_BAD_REQUEST)

class EhallDetailsView(APIView):
	def put(self, request, pk):
		try:
			#print pk
			hall_data 	=	Ehall.objects.get(pk = pk)
			get_data	=	request.data
			hall_data.name	=	get_data.get("name", hall_data.name)
			hall_data.area 	=	get_data.get("area", hall_data.area)
			hall_data.save()
			return Response("Successfully updated...", status.HTTP_200_OK)
		except Exception as exp:
			return Response(exp.message, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		try:
			data 	=	Ehall.objects.get(pk = id)
			data.hall_status	=	0
			data.save()
			return Response("Deleted successfully", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_304_NOT_MODIFIED)
	def get(self, request, id):
		try:
			data 	=	Ehall.objects.get(pk = id)
			h_data 	=	{"name":data.name, "area":data.area}
			#print h_data
			return Response(h_data, status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
########## STUDENT ###################################################################
class StudentView(APIView):
	def post(self, request):
		try:
			#s_data	=	Estudent(**request.data)
			s_data 	=	StudentSerailizer(data = request.data)
			print s_data
			if s_data.is_valid():		
				print '11111111111111111111111111111111'		
				s_data.save()
				return Response("Successfully student created11", status.HTTP_200_OK)
			else:
				print '2222222222222222222222222222222'
				return Response("Creation Failed", status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			print '33333333333333333333333333333333333'
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
class StudentDetailsView(APIView):
	def get(self, request, id):
		try:
			s_data		=	Estudent.objects.get(pk = id)
			get_data	=	{"name":s_data.name, "address":s_data.address, "phone":s_data.phone, "email":s_data.email}
			return Response(get_data, status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def put(self, request, id):
		try:
			s_data		=	Estudent.objects.get(pk = id)
			get_data 	=	request.data
			s_data.name	=	get_data.get("name", s_data.name)
			s_data.address	=	get_data.get("address", s_data.address)
			s_data.phone	=	get_data.get("phone", s_data.phone)
			s_data.email	=	get_data.get("email", s_data.email)
			s_data.save()			
			return Response("Student successfully updated", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		try:
			s_data		=	Estudent.objects.get(pk = id)
			s_data.student_status	=	0
			s_data.save()
			return Response("Student successfully deleted", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
########## COURSE ##################################################################################
class CourseView(APIView):
	def post(self, request):
		try:			
			c_data	=	Ecourse(**request.data)
			c_data.save()
			return Response("Successfully course created", status.HTTP_201_CREATED)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
class CourseDetailsView(APIView):
	def get(self, request, id):
		print id
		try:
			c_data	=	Ecourse.objects.get(pk = id)
			data 	=	{"name":c_data.name}
			return Response(data, status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def put(self, request, id):
		try:
			c_data	=	Ecourse.objects.get(pk = id)
			get_data	=	request.data
			c_data.name	=	get_data.get("name",c_data.name)
			c_data.save()
			return Response("Course successfully updated", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		try:
			c_data	=	Ecourse.objects.get(pk = id)			
			c_data.course_status	=	0
			c_data.save()
			return Response("Course successfully deleted", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
############ ENQUIRY ##############################################################
class EnquiryView(APIView):
	def post(slef, request):
		'''try:
			print request.data
			e_data	=	Eenquiry(**request.data)
			e_data.save()
			return Response("Enquiry created successfully", status.HTTP_201_CREATED)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
		'''
		try:
			print request.data
			e_data	=	EnqurySerializer(data = request.data)
			print '1111111111111111111111111111111111111111111111'
			print e_data
			print e_data.is_valid()
			print '1111111111111111111111111111111111111111111111'
			if e_data.is_valid():
				e_data.save()
				return Response("Enquiry created successfully", status.HTTP_201_CREATED)
			else:
				return Response("IS NOT VALID", status.HTTP_500_INTERNAL_SERVER_ERROR)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
class EnquiryDetailsView(APIView):
	def get(self, request, id):
		try:
			e_data	=	Eenquiry.objects.get(pk = id)
			data 	=	{"name":e_data.name, "course_id":e_data.course_id, "student_id":e_data.student_id}
			return Response(data, status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def put(self, request, id):
		try:
			e_data	=	Eenquiry.objects.get(pk = id)			
			get_data 	=	request.data
			
			print get_data
			#course_data		=	Ecourse.objects.get(get_data.course_id)
			#student_data	=	Estudent.objects.get(get_data.student_id)

			e_data.name			=	get_data.get("name", e_data.name)
			e_data.course_id	=	get_data.get("course_id", e_data.course_id)
			e_data.student_id	=	get_data.get("student_id", e_data.student_id)
			e_data.save()
			return Response("Enquiry successfully updated", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		try:
			e_data	=	Eenquiry.objects.get(pk = id)			
			e_data.enquiry_status	=	0
			e_data.save()
			return Response("Enquiry successfully deleted", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
################# EXPENSE ###################################################################
class ExpenseView(APIView):
	def post(self, request):
		try:
			ex_data		=	Eexpenses(**request.data)			
			ex_data.save()
			print "========== OK ====================="
			return Response("Expense successfully created", status.HTTP_201_CREATED)						
		except Exception as err:
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)
class ExpenseDetailsView(APIView):
	def get(self, request, id):
		try:
			ex_data		=	Eexpenses.objects.get(pk = id)			
			get_data	=	{"date":ex_data.date, "name":ex_data.name, "dec":ex_data.dec, "value":ex_data.value, "ehall_id":ex_data.ehall_id}
			return Response(get_data, status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def put(self, request, id):
		try:
			ex_data		=	Eexpenses.objects.get(pk = id)			
			get_data	=	request.data
			ex_data.date		=	get_data.get("date", ex_data.date)
			ex_data.name		=	get_data.get("name", ex_data.name)
			ex_data.dec			=	get_data.get("dec", ex_data.dec)
			ex_data.value		=	get_data.get("value", ex_data.value)
			ex_data.ehall_id	=	get_data.get("ehall_id", ex_data.ehall_id)
			ex_data.save()
			return Response("Expense successfully updated", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		try:
			ex_data		=	Eexpenses.objects.get(pk = id)			
			ex_data.exp_status	=	0			
			ex_data.save()
			return Response("Expense successfully deleted", status.HTTP_200_OK)
		except Exception as err:
			return Response(err.message, status.HTTP_400_BAD_REQUEST)

####################  EXPENSE SERIALIZER ################################################
class ExpenseSerializerView(APIView):
	def post(self, request):
		try:			
			expense_data 	=	ExpensesSerializer(data = request.data)
			print expense_data
			print '======================================'			
			#print expense_data.is_valid()
			print '======================================'			
			print '======================================'
			print expense_data.is_valid()
			print '======================================'
			if expense_data.is_valid():
				print '11111111111111'
				expense_data.save()
				return Response("Expense successfully created", status.HTTP_201_CREATED)
			else:
				print '2222222222222222'
				return Response("Expense details are not valid", status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			print '333333333333333333333333'
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)