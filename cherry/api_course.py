import requests
host		=	'http://127.0.0.1'
port		=	8001
base_url	=	"%s:%s/"%(host, port)

course1		=	base_url+"e_course/"
course2		=	base_url+"e_course/4/"
course3		=	base_url+"e_course/4/"
course4		=	base_url+"e_course/3/"
print 'begin 11111111111111111111111111111111111'
resp1		=	requests.post(course1, json={"name":"Honey"})
print resp1
print resp1.text
print resp1.status_code
print 'end 1111111111111111111111111111111111111'

print 'begin 22222222222222222222222222222222222'
resp2		=	requests.post(course2)
print resp2
print resp2.text
print resp2.status_code
print 'end 2222222222222222222222222222222222222'

print 'begin 33333333333333333333333333333333333'
resp3		=	requests.put(course3, json={"name":"Chinnu"})
print resp3
print resp3.text
print resp3.status_code
print 'end 3333333333333333333333333333333333333'

print 'begin 44444444444444444444444444444444444'
resp4		=	requests.delete(course4)
print resp4
print resp4.text
print resp4.status_code
print 'end 4444444444444444444444444444444444444'