from time import sleep

def Process():
	for i in range(5):
		print "Process 1........."
		sleep(1)
def NewProcess():
	for i in range(5):
		print "Process 2........."
		sleep(1)

Process()
NewProcess()