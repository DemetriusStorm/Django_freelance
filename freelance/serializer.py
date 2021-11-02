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
