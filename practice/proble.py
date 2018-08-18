import threading
from time import sleep
c = 0
def fun():
	global c
	print
	c = c+1
	print c
for i in range(10):
	pro = threading.Thread(target = fun, name = "{0}".format(i))
	pro.start()
	pro.join()