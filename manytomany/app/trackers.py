from .models import Trackerlogs
class RequestTrackerMiddleware:
	def __init__(self, viewfun):
		self.view_fun = viewfun
	def __call__(self, request):
		log_data 	=	Trackerlogs(path = request.get_raw_uri(), ip = request.META.get("REMOTE_ADDR"))
		log_data.save()
		print 'BEFORE CALL........................'
		print request.META.get('HTTP_X_FORWARDED_FOR')
		resp 	=	self.view_fun(request)
		print 'AFTER CALL.........................'
		return resp