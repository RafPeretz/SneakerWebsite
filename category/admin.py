from django.contrib import admin
from .models import Category

@admin.register(Category)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)
    list_per_page = 20

# admin.site.register(Category)

# Register your models here.
