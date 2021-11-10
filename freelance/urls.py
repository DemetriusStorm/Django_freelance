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
order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
    })
order_detail = OrderViewSet.as_view({'get': 'retrieve'})
# service_list = ServiceViewSet.as_view({
#     'get': 'list',
#     'post': 'create',    
# })
# service_detail = ServiceViewSet.as_view({'get': 'retrieve'})
# ordering_list = OrderingViewSet.as_view({
#     'get': 'list',
#     'post': 'create',    
# })
# ordering_detail = OrderingViewSet.as_view({'get': 'retrieve'})
message_list = MessageViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
message_detail = MessageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',    
})

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('executors/', executor_list, name='executor-list'),
    path('executors/<int:pk>', executor_detail, name='executor-detail'),
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:pk>', customer_detail, name='customer-detail'),
    path('order/', order_list, name='order-list'),
    path('order/<int:pk>', order_detail, name='order-detail'),
    # path('service/', service_list, name='service-list'),
    # path('service/<int:pk>', service_detail, name='service-detail'),
    # path('ordering/', ordering_list, name='ordering-list'),
    # path('ordering/<int:pk>', ordering_detail, name='ordering-detail'),
    path('message/', message_list, name='message-list'),
    path('message/<int:pk>', message_detail, name='message-detail'),
]
