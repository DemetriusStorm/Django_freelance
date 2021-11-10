from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *


class IsExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class LogOut(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Executor Views
class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Customer View
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Order Views
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# # Service Views
# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# # Ordering Views
# class OrderingViewSet(viewsets.ModelViewSet):
#     queryset = Ordering.objects.all()
#     serializer_class = OrderingSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Message Views
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
