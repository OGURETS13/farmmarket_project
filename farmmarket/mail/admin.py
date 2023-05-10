from django.contrib import admin

from mail.models import User, Product, Order, OrderItem, OrderStatus


admin.site.register(User)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(OrderStatus)
