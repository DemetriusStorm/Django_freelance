import pytest

from freelance.serializer import (
    ExecutorSerializer,
    OrderSerializer,
)


@pytest.mark.django_db
def test_valid_user_serializer():
    valid_serializer_data = {
        "user": {
            "username": "user_test",
            "email": "user_test1@test.usr",
            "first_name": "User",
            "last_name": "Test",
        },
        "phone": "89181510000"
    }

    executor_serializer = ExecutorSerializer(data=valid_serializer_data)

    assert executor_serializer.is_valid()
    assert executor_serializer.validated_data == valid_serializer_data
    assert executor_serializer.data == valid_serializer_data
    assert executor_serializer.errors == {}


