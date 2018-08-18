#import logging
#logging.basicConfig(level = logging.ERROR, format = "%(asctime)s--->%(levelname)s--->%(message)s", filename = "log.text")
#logging.info("1111")
#logging.error("2222")
#logging.warn("33333")
#logging.debug("4444")
def fun():
    print "this is function"
    c=100
    d=200
class EmpCompany:
    print "this is class"
    a=10
    b=20
    def sal_cal(emp):
        print "this is method inside the class"
        print emp
print EmpCompany.a
print EmpCompany.b
emp_instance = EmpCompany()
EmpCompany.sal_cal(emp_instance)

class a:
	c = 10
	d = 11
	def b(emp):
		print "Hello..."
print a.c
print a.d
instance = a()
a.b(instance)

class Customer:
	a = 10
	b = 11
	def getcustomer(cust):
		print "Get customer..."
print Customer.a
print Customer.b
######## 1
customer_instance = Customer()
Customer.getcustomer(customer_instance)
######## 2
Customer().getcustomer()
######## 3
customer_instance.getcustomer()
print Customer().a

a = "dad"
print a
print a[::-1]

class Emp:
	def __init__(self):
		print ">>>initialize..."
	def __sec__(self):
		print "kkkk"
	def getCustomer(self):
		print "customers..."
Emp().getCustomer()
Emp().__sec__()