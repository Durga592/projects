from rest_framework import serializers
from api.models import Eexpenses, Estudent
class ExpSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	Eexpenses
		fields	=	("id", "date", "name", "dec", "value", "exp_status", "ehall_id")

class StudentSerailizer(serializers.ModelSerializer):
	class Meta:
		model 	=	Estudent
		fields 	=	("id", "name", "address", "phone", "email")