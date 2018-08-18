import threading
from time import sleep

def fin1():
	print threading.current_thread()
	for i in range(5):		
		print "Hi1..........."
		sleep(1)
def fin2():
	print threading.current_thread()
	for i in range(5):		
		print "Hello........."
		sleep(1)

pro  = threading.Thread(target = fin1, name = "fin1")
pro1 = threading.Thread(target = fin2, name = "fin2")
pro.start()
pro1.start()
print threading.enumerate()
print threading.active_count()