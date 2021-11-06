from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *


executor_list = ExecutorViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
executor_detail = ExecutorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

customer_list = CustomerViewSet.as_view({'get': 'list'})
customer_detail = CustomerViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('executors/', executor_list, name='executor-list'),
    path('executors/<int:pk>', executor_detail, name='executor-detail'),
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:pk>', customer_detail, name='customer-detail'),
]
