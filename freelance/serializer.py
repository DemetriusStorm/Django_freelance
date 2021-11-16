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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')


class OrderTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = OrderTag
        fields = ('tag')


class OrderAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAttachment
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # attachments = OrderAttachmentSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderResponceSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()

    class Meta:
        model = OrderResponce
        fields = '__all__'


class OrderChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderChat
        fields = '__all__'


class OrderChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderChatMessage
        fields = '__all__'
