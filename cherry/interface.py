############# ONLY FOR STUDY HALL OPERATIONS ######################################################
import requests
host		=	'http://127.0.0.1'
port		=	8001
base_url	=	"%s:%s/"%(host, port)
consume_url			=	base_url+"e_hall/2/"
consume_url_one		=	base_url+"e_hall/"
consume_url_two		=	base_url+"e_hall/2/"
consume_url_three	=	base_url+"e_hall/2/"
resp		=	requests.post(consume_url)
resp1		=	requests.post(consume_url_one, json={"name":"Ramprakash", "area":"Chennai"})
resp2		=	requests.put(consume_url_two, json={"name":"Mithra", "area":"Hitech"})
resp3 		=	requests.delete(consume_url_three)
print '1111111111111111111111111111111111111111111 BEGIN.....'
print resp
print resp.text
print resp.status_code
print '1111111111111111111111111111111111111111111 END.......'

print '2222222222222222222222222222222222222222222 BEGIN.....'
print resp1
print resp1.text
print resp1.status_code
print '2222222222222222222222222222222222222222222 END.....'

print '3333333333333333333333333333333333333333333 BEGIN.....'
print resp2
print resp2.text
print resp2.status_code
print '3333333333333333333333333333333333333333333 END.....'

print '4444444444444444444444444444444444444444444 BEGIN.....'
print resp3
print resp3.text
print resp3.status_code
print '4444444444444444444444444444444444444444444 END.....'