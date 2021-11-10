from django.db import models
from django.contrib.auth.models import User


# Executor model
class Executor(models.Model):
    # Trigger on_delete for cascade delete all of the data user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'User: {self.user},  phone: {self.phone}'


# Customer model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'User: {self.user},  phone: {self.phone}'
