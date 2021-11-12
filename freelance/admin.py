from django.contrib import admin
from .models import *


admin.site.register(Executor)
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(OrderTag)
admin.site.register(OrderAttachment)
admin.site.register(OrderResponce)
admin.site.register(OrderChat)
admin.site.register(OrderChatMessage)
