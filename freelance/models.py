from django.db import models
from django.contrib.auth.models import User


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


# # Service model
# class Service(models.Model):
#     SERVICE_TYPES = [
#         ('1', 'Frontend'),
#         ('2', 'Backend'),
#     ]
#     executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     descr = models.CharField(max_length=1024)
#     price = models.IntegerField()

#     service_type = models.CharField(choices=SERVICE_TYPES, default='2', max_length=1)
#     # Ticket status
#     is_resolved = models.BooleanField(default=False)

#     def __str__(self):
#         # Use get_service_type_display func to display value
#         return f'{self.name}, {self.get_service_type_display()}, price: {self.price}'


# Order model
class Order(models.Model):
    # ORDER_TYPES = [
    #     ('1', 'Frontend'),
    #     ('2', 'Backend'),
    # ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    descr = models.CharField(max_length=1024)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=3)
    status = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return f'Order: {self.name}, status: {self.status}, price: {self.price}'


# # Ordering model to link
# class Ordering(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
#     order_date = models.DateTimeField()
#     deadline = models.DateTimeField()

#     def __str__(self):
#         return f'{self.order_date} - {self.deadline}, Customer - {self.customer}, Executor - {self.executor}.'
    

# Message model
class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    descr = models.CharField(max_length=1024)

    def __str__(self):
        return f'Message date: {self.msg_date}. Status: {self.is_edited}. Text: {self.descr}.'
