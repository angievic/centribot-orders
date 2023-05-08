from django.contrib import admin

from .models import Article,Order,OrderItem

admin.site.register(Article)
admin.site.register(Order)
admin.site.register(OrderItem)
