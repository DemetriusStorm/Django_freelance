import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    executor = User.objects.create_user(
        username='test_user',
        email='user1@test.usr',
        password='q1w2e3r4t5y',
    )
    assert executor.username == 'test_user'


@pytest.mark.django_db
def test_update_user():
    executor = User.objects.create_user(
        username='test_user',
        email='user1@test.usr',
        password='q1w2e3r4t5y',
    )
    executor.username = 'test_user5'
    executor.save()
    executor_from_db = User.objects.get(username = 'test_user5')
    assert executor_from_db.username == 'test_user5'
