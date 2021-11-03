from rest_framework import generics, viewsets, permissions, status
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


# Executor Views
class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer

class ExecutorUpdateView(generics.UpdateAPIView):
    # queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer
    permission_classes = (IsExecutor,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Executor.objects.filter(user=user)

        raise PermissionDenied()

class ExecutorCreateView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer

class ExecutorListView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


# Customer View
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
