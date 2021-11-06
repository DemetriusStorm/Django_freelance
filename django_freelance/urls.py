"""django_freelance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('freelance.urls')),
    path('openapi/', get_schema_view(
            title="Django Freelance",
            description="Description about Django Freelance API",
            version="1.0.0",
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='django_freelance/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
