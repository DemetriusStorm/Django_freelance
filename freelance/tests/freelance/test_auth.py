import pytest

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    user = User.objects.create_user(
        username='test_user',
        email='user1@test.usr',
        password='q1w2e3r4t5y',
    )
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client


@pytest.mark.django_db
def test_unauthorized(client):
    url = reverse('freelance:order-list')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request(api_client):
    url = reverse('freelance:executor-list')
    response = api_client.get(url)
    assert response.status_code == 200
