from django.contrib import admin
from .models import Category    
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'created_at', 'updated_at')
    list_display_links = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Category, CategoryAdmin)
