import logging
#logging.basicConfig(filename = "new_one.log", level = logging.INFO)
#logging.info("hum...")
s = "malayalam"
print s
print s[::-1]
print s.center(100, "*")
print s.capitalize()
print s.upper()
print s.lower()
print s.ljust(100, "*")
print s.rjust(100,"*")
logging.basicConfig(filename = "call_logs.log", format = "%(asctime)s %(module)s %(levelname)s %(message)s", level = logging.INFO)
logging.info("KKKKKKKKKKKK")
logging.error("helllo")
l1 = [1,2,3,4,5]
l2 = [3,4,6]
a = 0
b = []
for i in l2:
	if i in l1:
		#print i
		b.append(i)
		a+= i
print a
print b