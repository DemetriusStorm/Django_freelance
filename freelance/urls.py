from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    # path('auth/token/', obtain_auth_token, name='token'),
    # path('auth/logout', Logout.as_view()),

    path('executors/<int:pk>', ExecutorRetrieveView.as_view()),
    path('executors/update/<int:pk>', ExecutorUpdateView.as_view()),
    path('executors/all', ExecutorListView.as_view()),
    path('executors/new', ExecutorCreateView.as_view()),

    path('customers/<int:pk>', CustomerRetrieveView.as_view()),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view()),
    path('customers/all', CustomerListView.as_view()),
    path('customers/new', CustomerCreateView.as_view()),
]
