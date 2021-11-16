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

tags_list = TagViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})
order_attachment_list = OrderAttachmentViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
})
order_attachment_detail = OrderAttachmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})
order_customer_list = OrderCustomerViewSet.as_view({'get': 'list'})
order_executor_list = OrderExecutorViewSet.as_view({'get': 'list'})
order_responce_list = OrderResponceViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
})
order_chat_messages_list = OrderChatMessageViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
})
order_chat_detail = OrderChatViewSet.as_view({'get': 'retrieve'})

app_name = 'freelance'
urlpatterns = [
    # path('auth/', include('djoser.urls'), name='current_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('executors/', executor_list, name='executor-list'),
    path('executors/<int:pk>', executor_detail, name='executor-detail'),
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:pk>', customer_detail, name='customer-detail'),
    path('tags/', tags_list, name='tag-list'),
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>', order_detail, name='order-detail'),
    path('orders/executor/', order_executor_list, name='order-executor-list'),
    path('orders/customer/', order_customer_list, name='order-customer-list'),
    path('orders/<int:pk>/responce/', order_responce_list, name='order-responce-detail'),
    # path('orders/<int:pk>/responce/<int:pk>/status/', ...),
    path('order/<int:pk>/chat/', order_chat_detail, name='order-chat-list'),
    path('order/<int:pk>/chat/messages/', order_chat_messages_list, name='order-chat-messages-detail'),
]
