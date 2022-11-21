from django.contrib import admin
from . models import *

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'title_g', 'quantity', 'price','order_no', 'amount', 'paid', 'created_at']
admin.site.register(Cart, CartAdmin)
