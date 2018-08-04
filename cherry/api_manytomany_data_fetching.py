#from rest_framework.parsers import JSONParser
import requests
import json
host		=	'http://127.0.0.1'
port 		=	8003
base_url	=	"%s:%s/"%(host, port)
get_order_details	=	base_url+"order_details/"
resp 		=	requests.get(get_order_details, auth=("nani", "12j11d5819"), headers = {"Authorization" : "Token a37fde445d8aca194de6cd3d02c04fdb47b1b798"})
print resp
print resp.text
print resp.status_code
fin_res 	=	 json.loads(resp.text)
'''print fin_res
for j in fin_res:
	for p in j['product']:
		print "id %s | name %s | customer %s | product %s "%(j['id'] , j['name'], j['customer'], p)
'''