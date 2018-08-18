import pandas as pd 
import matplotlib.pyplot as plt 
person_info = [	{'id':1, 'name':'Nani', 'sal':300000},
				{'id':5, 'name':'Chinnu', 'sal':400000},
				{'id':4, 'name':'Kanna', 'sal':900000},
				{'id':6, 'name':'Honey', 'sal':600000},
				{'id':3, 'name':'Chinna', 'sal':200000},
				{'id':10, 'name':'Sweety', 'sal':500000},
				{'id':9, 'name':'Angel', 'sal':100000},
				{'id':8, 'name':'Gold', 'sal':800000},
				{'id':7, 'name':'Mammu', 'sal':500000},
				{'id':2, 'name':'Chiiti', 'sal':700000},
			]
data 	=	pd.DataFrame(person_info)
print data