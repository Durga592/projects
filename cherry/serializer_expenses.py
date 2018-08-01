import requests
host			=	'http://127.0.0.1'
port			=	8001
base_url		=	"%s:%s/"%(host, port)

serialize_url	=	base_url+"e_expense_serializer/"
resp			=	requests.post(serialize_url, json={"name":"milk2121", "value":"250", "ehall_id":"2", "exp_status":"1"})
print resp
print resp.text
print resp.status_code