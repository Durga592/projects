from rest_framework import serializers
from app.models import Customer, Product, Order

class Customerserializer(serializers.ModelSerializer):
	class Meta:
		model 		=		Customer
		fields 		=		("id", "name")

	def validate_name(self, value):
		if value.isalpha():
			return value
		raise serializers.ValidationError("Name should contain only alphabets")

class Productserializer(serializers.ModelSerializer):
	class Meta:
		model 		=		Product
		fields 		=		("id", "name")

class Orderserializer(serializers.ModelSerializer):
	#product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
	class Meta:
		model 		=		Order
		fields 		=		("id", "product", "customer", "name")

class DetailsOrderserializers(serializers.ModelSerializer):
	#product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
	class Meta:
		model 		=		Order
		fields 		=		'__all__'