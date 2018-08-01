from rest_framework import serializers
from api.models import Eexpenses, Estudent, Eenquiry, New
class ExpSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	Eexpenses
		fields	=	("id", "ehall", "date", "name", "dec", "value", "exp_status")

class StudentSerailizer(serializers.ModelSerializer):
	class Meta:
		model 	=	Estudent
		fields 	=	("id", "name", "address", "phone", "email")

class ExpensesSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	Eexpenses
		fields 	=	("id", "date", "name", "dec", "value", "exp_status", "ehall")

class EnqurySerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	Eenquiry
		fields 	=	("id", "name", "enquiry_status", "course", "student")

class NewSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	New
		fields 	=	("name", "ehall")