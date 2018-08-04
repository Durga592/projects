from .models import RequestTracker
class RequestTrackerMiddleware:
	def __init__(self, viewfun):
		self.view_fun 	=	viewfun
	def __call__(self, request):
		#import pdb; pdb.set_trace()
		rt 	=	RequestTracker(path = request.get_raw_uri(), ip = request.META.get("REMOTE_ADDR"))
		rt.save()
		print "before processing"
		resp 	=	self.view_fun(request)  #WE ARE PROCESSING
		print "after processing, before sending response, we can write something"
		return resp