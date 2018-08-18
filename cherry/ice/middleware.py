from .models import RequestTracker
class RequestTrackerMiddleware:
	def __init__(self, viewfun):
		self.view_fun 	=	viewfun
	def __call__(self, request):
		#import pdb; pdb.set_trace()
		rt 	=	RequestTracker(path = request.get_raw_uri(), ip = request.META.get("REMOTE_ADDR"))		
		rt.save()
		print "before processing"	
		print rt.status
		resp 	=	self.view_fun(request)  #WE ARE PROCESSING
		rt.status = resp.status_code
		if resp.status_code == 400:
			print "|||||||||| ok ||||||||||||||||"
		print resp
		print "after processing, before sending response, we can write something"
		return resp