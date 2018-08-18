# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Customer, Product, Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from serializers import Customerserializer, Productserializer, Orderserializer, DetailsOrderserializers
from django.db import connection
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework import authentication
#from rest_framework.permissions import AllowAny
import logging
log = logging.getLogger(__name__)
# Create your views here.

########### FOR OPTIONAL AUTHENTICATION ###############################
@authentication_classes([])
@permission_classes([])
########### FOR OPTIONAL AUTHENTICATION ###############################
class Customercreation(APIView):
	#permission_classes 	=	(permissions.IsAuthenticated,)	
	#@permission_classes((AllowAny, ))
	def post(self, request):
		try:
			print 'hellooooooooooooooooooo.....'
			c_data		=		Customerserializer(data = request.data)
			if c_data.is_valid():
				print 'okkkkkkkkkkkkkkkkkk.....'
				c_data.save()
				return Response("Customer successfully created", status.HTTP_201_CREATED)
			else:
				return Response(c_data._errors, status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Productcreation(APIView):
	def post(self, request):
		try:
			p_data 		=		Productserializer(data = request.data)
			if p_data.is_valid():
				p_data.save()
				return Response("Product successfully created", status.HTTP_201_CREATED)
			else:
				return Response("Product creation failed", status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)

########### FOR OPTIONAL AUTHENTICATION ###############################
@authentication_classes([])
@permission_classes([])
########### FOR OPTIONAL AUTHENTICATION ###############################
class Ordercreation(APIView):
	def post(self, request):
		try:
			o_data		=	Orderserializer(data = request.data)
			print 'ORDER...................'
			print o_data
			print o_data.is_valid()
			print 'ORDER ENDING .......................'
			if o_data.is_valid():
				get_id 	=	o_data.save()
				print 'QUERY STARTED...................................'
				print connection.queries
				print 'QUERY END...................................'
				print 'GET ID BEGIN....................................'
				print get_id.id
				print 'GET ID END....................................'
				return Response("Order successfully created", status.HTTP_201_CREATED)
			else:
				return Response("Order creation failed", status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Orderoperationdetails(APIView):
	######### AT A TIME TWO AUTHENTICATION IS NOT POSSIBLE ##############################################
	#authentication_classes 	=	(authentication.TokenAuthentication,)
	#permission_classes 	=	(permissions.IsAuthenticated,)	
	def get(self, request):
		try:
			log.info(">>>>>>>>>>>>>>>started")
			get_data 		=	Order.objects.all()
			#print 'NORMAL BEGIN ............................'
			#print get_data
			#print 'NORMAL END...............................'
			print log.error(">>>>>>>>>>>>>>>>>.test")
			print log.debug('=========================ok')
			#print log.warning("<<<<<<<<<<<<<<<<<< WARNING")
			#print log.critical("&&&&&&&&&&&&&&&&&&&&&&& CRITICAL")
			serializer	=	DetailsOrderserializers(Order.objects.all(), many=True)
			#print 'query begin..........................................'
			#print connection.queries
			#print 'query ending..........................................'
			#json 			=	JSONRenderer().render(order_details.data)
			#print 'SERIALIZERS BEGIN .................................'
			#print serializer
			#print 'NO.................................................'
			#print json
			send_data 	=	serializer.data
			#print send_data
			#print 'SERIALIZERS END....................................'

			return Response(send_data, status.HTTP_200_OK)			
		except Exception as err:
			log.error(err.message)
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)