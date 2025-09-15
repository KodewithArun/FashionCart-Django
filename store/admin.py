from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available', 'category', 'created_at', 'updated_at')
    list_display_links = ('product_name', 'slug')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name', 'category__category_name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

admin.site.register(Product, ProductAdmin)
