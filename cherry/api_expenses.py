import requests
import datetime
host		=	'http://127.0.0.1'
port		=	8001
base_url	=	"%s:%s/"%(host, port)

ex1		=	base_url+"e_expense/"
ex2		=	base_url+"e_expense/2/"
ex3		=	base_url+"e_expense/1/"
ex4		=	base_url+"e_expense/1/"
print 'begin 11111111111111111111111111111111111'
resp1		=	requests.post(ex1, json={"date":'2018-07-31 10:10:10.900000', "name":"milk", "dec":"fine", "value":"250", "ehall_id":"2"})
print resp1
print resp1.text
print resp1.status_code
print 'end 1111111111111111111111111111111111111'

print 'begin 22222222222222222222222222222222222'
resp2		=	requests.get(ex2)
print resp2
print resp2.text
print resp2.status_code
print 'end 2222222222222222222222222222222222222'

print 'begin 33333333333333333333333333333333333'
resp3		=	requests.put(ex3, json={"date":'2018-07-30 10:10:10.900000', "name":"milk roties", "dec":"fine ok", "value":"350", "ehall_id":"3"})
print resp3
print resp3.text
print resp3.status_code
print 'end 3333333333333333333333333333333333333'

print 'begin 44444444444444444444444444444444444'
resp4		=	requests.delete(ex4)
print resp4
print resp4.text
print resp4.status_code
print 'end 4444444444444444444444444444444444444'