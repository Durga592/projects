# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# FOR CSS JS FILES CALLING
from django.conf.urls.static import static
######## FOR USER CREATION & Permission FOR USER PERMISSIONS #######################
from django.contrib.auth.models import Permission, User
#FOR USER AUTHUNETICATION(LOGIN & LOGOUT)
from django.contrib.auth import authenticate, login, logout
#FOR LOGIN ACCESS FOR PAGES
from django.contrib.auth.decorators import login_required, permission_required
######## FOR FILE UPLOADING & Document FOR USER PERMISSIONS ###############################
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from ice.models import Document, Studyhall
from ice.forms import DocumentForm
######## FOR USER PERMISSIONS #############################
import os, datetime, time
import requests
from django.http import HttpResponse
#from django.contrib.contenttypes.models import ContentType
#from django.shortcuts import get_object_or_404

# Create your views here.
########## USER PERMISSIONS ##########################################################
#def user_gains_perms(request, user_id):
#	user = get_object_or_404(User, pk=user_id)

def user_login(f, *args1):
	def inner(*args):
		print 'args begin....'
		print args[0].session
		print args[0].session.items()
		print 'kkkkkkk'
		print args
		print 'kkkkkkk'
		print 'args end....'
		if "_auth_user_id" in args[0].session:
			print 'one....'
			return f(*args)
		else:
			print 'twoooo'
			return redirect(get_logout)
	return inner

@login_required(login_url = '/login/')
#@permission_required('can_vote', login_url = '/login/')
#@permission_required('add_document', raise_exception=True)
#@user_login
def get_dashboard(request):
	print request.COOKIES
	#import pdb; pdb.set_trace()
	print request.session
	response 	=	render(request, "ice/dashboard.html")	
	return response
def get_logout(request):
	print request.session.items()
	#request.session.clear()
	logout(request)	
	print "GET RESPONSE BEGIN..."	
	print "GET RESPONSE END..."
	print 'COOKIES............... BEGIN'
	print request.COOKIES
	print 'COOKIES............... END'	
	response 	=	 redirect("/login/")
	#response.COOKIES.clear()
	#response.COOKIES.pop('login_user')
	response.delete_cookie('login_user')
	return response

def get_login(request, *args, **kwargs):	
	#import pdb; pdb.set_trace()
	print 'helllo.........'
	print args
	print kwargs
	print request.POST.get('next')
	print request.user
	print request.session.items()	
	print request.COOKIES
	print 'helloo.........'
	if "_auth_user_id" in request.session:
		return redirect("/dashboard/")
	else:
		user_res 	=	''
		if request.method == 'POST':
			user_res 	=	authenticate(username = request.POST['username'].strip(), password = request.POST['password'].strip())			
			if user_res:
				#import pdb; pdb.set_trace()
				#request.session.update({"user":user_res.id})
				login(request, user_res)
				#response	=	render(request, template)
				#user_res.set_cookie('login_user', 0)
				print request.session.items()
				response	=	 redirect("/dashboard/")
				response.set_cookie('login_user', user_res)
				return response
			else:			
				return render(request, "ice/login.html", {"suc_msg":'Login failed'})	
		return render(request, "ice/login.html")
@login_required(login_url = '/login/')
#@user_login
def user_registration(request):
	#if "user" in request.session:
		msg		=	''
		if request.method == 'POST':
			get_user	=	User.objects.create_user(username = request.POST['username'], 
														password = request.POST['password'], 
														email = request.POST['email'])
			if get_user:
				msg		=	'User created successfully'
			else:
				msg 	=	'User creation failed'
		return render(request, "ice/register.html", {"suc_msg":msg})
	#else:
		#return redirect("/get_logout/")
#######################################################################################################
################## FILE UPLOADING BEGIN HERE #################################################################
@login_required(login_url = '/login/')
def model_form_upload(request):
	print request.session['_auth_user_id']
	if request.method == 'POST':
		print request.FILES
		print request.POST
		user_instance	=	User.objects.get(pk = request.session['_auth_user_id'])
		form = DocumentForm(request.POST, request.FILES)
		form.created_id = user_instance
		print 'begin---------------------'
		print form
		print 'end-----------------------'
		#import pdb; pdb.set_trace()
		if form.is_valid():
			form.save()
			return redirect(get_uploadedfiles)
	else:
		form = DocumentForm()
	return render(request, 'ice/model_form_upload.html', {'form': form})
@login_required(login_url = '/login/')
def get_uploadedfiles(request):
	documents = Document.objects.all()
	return render(request, 'ice/home.html', { 'documents': documents })
################## FILE UPLOADING ENDING HERE #################################################################
#######################################################################################################
@login_required(login_url = '/login/')
def get_studyhall(request):	
	msg 	=	''
	if request.method == 'POST':
		user_instance	=	User.objects.get(id = request.session['_auth_user_id'])
		print 'begin user........'
		print user_instance
		print 'end user........'
		print datetime.datetime.now()
		pic 	=	request.FILES.get('pic')
		#pic = request.FILES.get("hall_pic")
		'''
		name=str(time.time())+pic.name
		#path = os.path.join(settings.MEDIA_ROOT,name)		
		f=open(path,"wb")
		for chunk in pic.chunks():
			f.write(chunk)
		f.close()
		'''		
		#import pdb; pdb.set_trace()
		hall_instance	=	Studyhall(name			=	request.POST['h_name'],
										area		=	request.POST['h_area'],
										doc_name	=	pic,
										created_id	=	request.session['_auth_user_id'],
										created_at	=	datetime.datetime.now())
		hall_instance.save()
		msg 	=	'Successfully hall created'
	return render(request, "ice/studyhall.html", {"suc_msg":msg})

def api_call(request):
	url 	=	'http://127.0.0.1:8001/e_hall/'
	res 	=	requests.get(url)
	return HttpResponse(res)