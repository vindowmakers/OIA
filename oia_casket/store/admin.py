from django.contrib import admin
from .models import Casket, Order, OrderItem

admin.site.register(Casket)
admin.site.register(Order)
admin.site.register(OrderItem)
