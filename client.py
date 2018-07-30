import requests
import os
username	=	"pillamdurga592@gmail.com"
password	=	"12j11d5819"
resp		=	requests.get("https://api.github.com/users/Durga592/orgs", auth = (username, password))
print resp
import pdb; pdb.set_trace()