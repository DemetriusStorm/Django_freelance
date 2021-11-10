from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('executors/<int:pk>', ExecutorRetrieveView.as_view()),
    path('executors/<int:pk>', ExecutorUpdateView.as_view()),
    path('executors/', ExecutorListView.as_view()),
    path('executors/', ExecutorCreateView.as_view()),

    path('customers/<int:pk>', CustomerViewSet.as_view()),
    path('customers/', CustomerViewSet.as_view()),
]
