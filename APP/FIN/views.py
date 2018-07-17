# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp, Userdets
from django.contrib.auth.hashers import PBKDF2PasswordHasher, SHA1PasswordHasher
#from ipware.ip import get_ip_address_from_request

# Create your views here.
def get_fin_users(request):
	#return HttpResponse("welcome message...")
	msg=""
	#print request.session["fav_color"]
	#print request.session.modified
	#print request.session.keys()
	#del request.session["fav_color"]
	#print "key is begin"
	#print request.session["fav_color"]
	#print "key is ending"
	print request.session.session_key
	if request.method=="POST":
		data = request.POST
		emp_instance=Emp(name=data['name'],
			age=data['age'],
			sala=data["sala"])
		emp_instance.save()
		msg="Successfully inserted"
	data = Emp.objects.all()
	return render(request, "home.html",{"message":msg,"data":data})
	
def empdrop(request, empid):
	emp_instance	=	Emp.objects.get(id = empid)
	emp_instance.delete()
	return redirect("/fin_users/")	

def empsearch(request):
	emp_name			=	''
	search_data			=	''
	ses					=	''
	request.session["fav_color"] = "blue2"	
	#print request.session["fav_color"]
	#if	request.session["fav_color"]	==	'blue2':
	#	print "hello"
	if request.method	==	'POST':
		get_data		=	request.POST
		emp_name		=	get_data['name']
		search_data		=	Emp.objects.filter(name__contains=emp_name)
		print dir()
		#search_data		=	Emp.objects.all()		
	return render(request, "search_employee.html", {"name":emp_name, "data":search_data, "session":ses})

def userreg(request):
	succ_msg	=	''
	print request.method
	print request.POST
	if request.method	==	'POST':
		data			=	request.POST
		user_instance	=	Userdets(name		=	data['name'],
								username	=	data['username'],
								password	=	data['password'],
								mailid		=	data['mailid'])
		user_instance.save()
		succ_msg		=	'User Successfully Created'
	get_data			=	Userdets.objects.all()
	return render(request, "user_reg.html", {"msg":succ_msg})

def userlogin(request):
	login_user	=	''
	res			=	''
	res_msg		=	''	
	print request.method
	print request.POST
	if request.method	==	'POST':
		data		=	request.POST
		user_name	=	data['username']
		pass_word	=	data['password']
		print user_name
		print pass_word
		res			=	Userdets.objects.get(username = user_name, password = pass_word)
		print res.id
		if res.id >0:
			request.session['user_id']	=	res.id
			request.session.set_expiry(300)			
			res_msg	=	'User Login Successfully'
			#return render(request, "get_dashboard.html", {"suc_msg":res_msg})
			return redirect('/dashboard/')
		else:
			res_msg	=	'User Login Failed'	
	#if	request.session['user_id']	>0	:
	if 'user_id' in request.session:
		print "ses created..."
		print request.session['user_id']
	else:
		print "sess not created..."
	sesval  =   request.session.session_key
	#del request.session[sesval]
	#request.session['user_id']
	print sesval
	return render(request, "user_login.html", {"user_details":login_user, "login_res":res, "res_show_msg":res_msg})

def get_dashboard(request):
	response 	 =	render(request, "get_dashboard.html")
	#ip 			 =	get_client_ip(request) #GET RUNNING APPLICATION IP ADDRESS ONLY...
	#ip 			=	get_my_ip(request) #GET RUNNING APPLICATION IP ADDRESS ONLY...
	#user_ip  =  get_ip_address_from_request(request)
	#user_ip   = get_geo_ip(request)
	user_ip    =  request.META.get('HTTP_X_REAL_IP')
	print user_ip
	if 'user_id' in request.session:
		print request.session['user_id']
		print request.session.session_key
		userid 		=	request.session['user_id']
		res_data	=	Userdets.objects.get(id = userid)
		#res_data.username
		response.set_cookie('login_user', res_data.username, 3600 * 24 * 365 * 2)	
	else:
		return redirect('/user_login/')	
	return response
	#return render(request, "get_dashboard.html")

def get_logout(request):
	response 	 =	render(request, "get_dashboard.html")
	if 'user_id' in request.session:
		print request.session['user_id']
	else:
		pass
	try:
		if 'user_id' in request.session:	
			userid 		=	request.session['user_id']
			get_data 	=	Userdets.objects.get(id = userid)	
			sesval	=	request.session.session_key
			print sesval
			#get_data.username
			response.delete_cookie('1234')
			#del request.session[sesval]           	
			del request.session['user_id']	
			#del request.session.pop['0jeo0kuiw07m2bc6ra4gf8ft3ffp6qgo', None]
			print 'ok...'
			if 'user_id' not in request.session:
				print "user logedout and sess destroyed successfully"
				return redirect('/user_login/')
			else:
				pass
		else:
			print 'sess not destroyed...'
			return redirect('/user_login/')
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

def track_user(request):
    if not request.COOKIES.get('visits'):
        response = HttpResponse("This is your first visit to the site. "
                                "From now on I will track your vistis to this site.")
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits')) + 1
        response = HttpResponse("This is your {0} visit".format(visits))
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response

def track_user1(request):
	if not request.COOKIES.get('visits'):		
		print request.COOKIES.get('visits')

#GET URL IP ADDRESS ONLY...
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def get_geo_ip(request): 
	#ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDER_FOR', '') 
	ip  = request.META.get('HTTP_X_FORWARDER_FOR', '') 
	return ip