import threading
from time import sleep
c = 0
def fun1():
	global c
	for i in range(10):
		print "thread {0}".format(i)
		print threading.current_thread()
		c = c+1
		sleep(1)
	print c
thr1 = threading.Thread(target = fun1, name = "t1")
thr2 = threading.Thread(target = fun1, name = "t2")
thr1.start()
thr1.join()
thr2.start()