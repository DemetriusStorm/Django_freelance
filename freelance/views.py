from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


from .models import *
from .serializer import *


class IsExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class LogOut(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Executor View
class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Customer View
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderTag.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Tag View
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order attach View
class OrderAttachmentViewSet(viewsets.ModelViewSet):
    queryset = OrderAttachment.objects.all()
    serializer_class = OrderAttachmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Order customer View
class OrderCustomerViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order executor View
class OrderExecutorViewSet(viewsets.ModelViewSet):
    queryset = OrderResponce.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order responce View
class OrderResponceViewSet(viewsets.ModelViewSet):
    queryset = OrderResponce.objects.all()
    serializer_class = OrderResponceSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order chat View
class OrderChatViewSet(viewsets.ModelViewSet):
    queryset = OrderChat.objects.all()
    serializer_class = OrderChatSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Order chat message View
class OrderChatMessageViewSet(viewsets.ModelViewSet):
    queryset = OrderChatMessage.objects.all()
    serializer_class = OrderChatMessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
