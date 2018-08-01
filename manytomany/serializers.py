from rest_framework import serializers
from app.models import Customer, Product, Order

class Customerserializer(serializers.ModelSerializer):
	class Meta:
		model 		=		Customer
		fields 		=		("id", "name")

class Productserializer(serializers.ModelSerializer):
	class Meta:
		model 		=		Product
		fields 		=		("id", "name")

class Orderserializer(serializers.ModelSerializer):
	#product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
	class Meta:
		model 		=		Order
		fields 		=		("id", "product", "customer", "name")