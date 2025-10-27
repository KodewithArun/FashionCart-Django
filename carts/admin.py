from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

admin.site.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created_at', 'updated_at')
    search_fields = ('cart_id',)
    ordering = ('-created_at',)
    
admin.site.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('cart__cart_id', 'product__name')
    ordering = ('-cart__created_at',)
    