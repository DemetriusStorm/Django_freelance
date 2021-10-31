from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Executor model
class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Trigger on_delete for cascade delete all of the data user
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'User: {self.user},  phone: {self.phone}'


# Customer model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'User: {self.user},  phone: {self.phone}'
