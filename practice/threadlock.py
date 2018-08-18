import threading
from time import sleep
c = 0
lock = threading.Lock()
def fun1():
	global c, lock
	lock.acquire()	
	c = c+1
	print c
	lock.release()
s = threading.Thread(target=fun1)
s.start()