import threading
from time import sleep

def Process():
	for i in range(5):
		print "Process"
		sleep(1)
def Newprocess():
	for i in range(5):
		print "New Process"
		sleep(1)

pro1 	=	threading.Timer(10, Process)
pro2 	=	threading.Thread(target = Newprocess)

pro1.start()
pro2.start()
print threading.enumerate()
print pro1.is_alive()
#status_check()