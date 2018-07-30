import requests
hostname	=	"http://127.0.0.1"
port		=	8000
base_url	=	"%s:%s/"%(hostname, port)
print 'begin------------------------------'
print base_url
print 'end--------------------------------'
#import pdb;pdb.set_trace()
study_hall_url	=	base_url+"studyhall/"
resp 	=	requests.get(study_hall_url)
print resp
