import threading
from time import sleep
c = 0
lock = threading.Lock()
def fun():	
	global c, lock
	print threading.current_thread()
	#lock.acquire()
	#sleep(1)
	c = c+1
	print c
	#lock.release()
for i in range(10):
	t = threading.Thread(target = fun)
	t.start()
