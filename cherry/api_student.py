import requests
host		=	'http://127.0.0.1'
port		=	8001
base_url	=	"%s:%s/"%(host, port)

fun_url1	=	base_url+"e_student/"
fun_url2	=	base_url+"e_student/2/"
fun_url3	=	base_url+"e_student/3/"
fun_url4	=	base_url+"e_student/7/"
print 'block 1111111111111111111111111111.........'
resp1		=	requests.post(fun_url1, json={"name":"Nani4", "address":"Hyd4", "phone":"4987698798", "email":"nani4@gmail.com"})
print resp1
print resp1.text
print resp1.status_code
print 'block 111111111111111111111111111..........'

print 'block 222222222222222222222222222.........'
resp2		=	requests.post(fun_url2)
print resp2
print resp2.text
print resp2.status_code
print 'block 222222222222222222222222222..........'

print 'block 333333333333333333333333333.........'
resp3		=	requests.put(fun_url3, json={"name":"Nani1", "address":"Hyd1", "phone":"1987698798", "email":"nani1@gmail.com"})
print resp3
print resp3.text
print resp3.status_code
print 'block 333333333333333333333333333..........'

print 'block 444444444444444444444444444.........'
resp3		=	requests.delete(fun_url4)
print resp3
print resp3.text
print resp3.status_code
print 'block 444444444444444444444444444..........'
