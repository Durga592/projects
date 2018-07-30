import requests
hostname	=	'http://127.0.0.1'
#hostname	=	'0.0.0.0'
port		=	8000
base_url	=	"%s:%s/"%(hostname, port)
e_hall_url	=	base_url+"e_hall/"
resp		=	requests.get(e_hall_url)
print resp