import threading
from time import sleep
c = 0
sem = threading.Semaphore()
def fun():	
	global c, sem
	print threading.current_thread()
	sem.acquire()
	#sleep(1)
	c = c+1
	print c
	sem.release()
for i in range(10):
	t = threading.Thread(target = fun)
	t.start()
