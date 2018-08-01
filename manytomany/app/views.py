# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Customer, Product, Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import Customerserializer, Productserializer, Orderserializer
# Create your views here.

class Customercreation(APIView):
	def post(self, request):
		try:
			print 'hellooooooooooooooooooo.....'
			c_data		=		Customerserializer(data = request.data)
			if c_data.is_valid():
				print 'okkkkkkkkkkkkkkkkkk.....'
				c_data.save()
				return Response("Customer successfully created", status.HTTP_201_CREATED)
			else:
				return Response("Customer creation failed", status.HTTP_400_BAD_REQUEST)
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

class Ordercreation(APIView):
	def post(self, request):
		try:
			o_data		=	Orderserializer(data = request.data)
			print 'ORDER...................'
			print o_data
			print o_data.is_valid()
			print 'ORDER ENDING .......................'
			if o_data.is_valid():
				o_data.save()
				return Response("Order successfully created", status.HTTP_201_CREATED)
			else:
				return Response("Order creation failed", status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message, status.HTTP_500_INTERNAL_SERVER_ERROR)