from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ExecutorSerializer(serializers.ModelSerializer):
    # Link to User serializer to fetch all data
    user = UserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'  # Use all fields


# Let's create serializer with only id without link to User
class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Customer
        fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# class ServiceSerializer(serializers.ModelSerializer):
#     executor = ExecutorSerializer()
#     service_type = serializers.CharField(source='get_service_type_display')
    
#     class Meta:
#         model = Service
#         fields = '__all__'


# class CreateServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_type = serializers.CharField(source='get_order_type_display')
    
    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# class OrderingSerializer(serializers.ModelSerializer):
#     service = ServiceSerializer()
#     order = OrderSerializer()
#     customer = CustomerSerializer()
#     executor = ExecutorSerializer()
    
#     class Meta:
#         model = Ordering
#         fields = '__all__'


# class CreateOrderingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ordering
#         fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    
    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
