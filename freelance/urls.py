from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='token'),
]
