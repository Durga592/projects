from rest_framework import serializers
from api.models import Eexpenses
class ExpSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	Eexpenses
		fileds	=	("id", "date", "name", "dec", "value", "ehall_id")