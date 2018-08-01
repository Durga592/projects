import requests
host		=	'http://127.0.0.1'
port		=	8003
base_url	=	"%s:%s/"%(host, port)

customer_url	=	base_url+"customer/"

resp			=	requests.post(customer_url, json={"name":"Gold"})
print resp
print resp.text
print resp.status_code

product_url		=	base_url+"product/"
resp1			=	requests.post(product_url, json={"name":"ERP tools"})
print resp1
print resp1.text
print resp1.status_code

order_url		=	base_url+"order/"
resp2			=	requests.post(order_url, json={"product":[3,4], "customer":"1", "name":"OTA"})
print resp2
print resp2.text
print resp2.status_code