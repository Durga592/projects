import requests
host		=	'http://127.0.0.1'
port		=	8001
base_url	=	"%s:%s/"%(host, port)

en1		=	base_url+"e_enquiry/"
en2		=	base_url+"e_enquiry/2/"
en3		=	base_url+"e_enquiry/1/"
en4		=	base_url+"e_enquiry/1/"
print 'begin 11111111111111111111111111111111111'
resp1		=	requests.post(en1, json={"name":"Course", "course_id":"1", "student_id":"2"})
print resp1
print resp1.text
print resp1.status_code
print 'end 1111111111111111111111111111111111111'

print 'begin 22222222222222222222222222222222222'
resp2		=	requests.post(en2)
print resp2
print resp2.text
print resp2.status_code
print 'end 2222222222222222222222222222222222222'

print 'begin 33333333333333333333333333333333333'
resp3		=	requests.put(en3, json={"name":"New Course", "course_id":"2", "student_id":"2"})
print resp3
print resp3.text
print resp3.status_code
print 'end 3333333333333333333333333333333333333'

print 'begin 44444444444444444444444444444444444'
resp4		=	requests.delete(en4)
print resp4
print resp4.text
print resp4.status_code
print 'end 4444444444444444444444444444444444444'