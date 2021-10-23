from django.contrib import admin

from .models import RealEstate, Review, Order, OrderItem, ShippingAddress

admin.site.register(RealEstate)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
