from django.db import models
from django.contrib.auth.models import User

import enum


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


# Orders section
OrderStatus = enum.Enum(
    'OrderStatus', (
        'NEW', 'PUBLISHED', 'IN_PROCESS', 'COMPLETED_WITH_SUCCESS', 'COMPLETED_WITH_FAIL'), start=0)
OrderResponceStatus = enum.Enum(
    'Responce', (
        'NEW', 'ACCEPTED', 'DECLINED', 'WITHDRAWN'), start=0)

ORDER_STATUS_CHOICES = tuple(map(lambda x: (x.value, x.name), OrderStatus))
ORDER_RESPONCE_STATUS_CHOICES = tuple(
    map(lambda x: (x.value, x.name), OrderResponceStatus),
)


class Tag(models.Model):
    tag = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='tag_creator',
    )

    class Meta:
        db_table = 'tag'


# Order model
class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    customer = models.ForeignKey(
        Customer,
        related_name='order_customer',
        on_delete=models.CASCADE,
    )
    executor = models.ForeignKey(
        Executor,
        related_name='order_executor',
        on_delete=models.CASCADE, null=True,
    )
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'


# Order tag model
class OrderTag(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='order_tag_key',
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_tag',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_tag'


# Order attach
class OrderAttachment(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='attachments',
        on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    filename = models.TextField()
    # sha1 hash
    hash = models.CharField(max_length=40)
    # max url length is 2000
    url = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_attachment'


# Order response model
class OrderResponce(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_responce',
    )
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=ORDER_RESPONCE_STATUS_CHOICES,
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_responce'


# Order message model
class OrderChat(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    messages_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_chat'


class OrderChatMessage(models.Model):
    chat = models.ForeignKey(
        OrderChat,
        related_name='messages',
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    sender = models.ForeignKey(User, related_name='order_chat_sender')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_chat_message'
