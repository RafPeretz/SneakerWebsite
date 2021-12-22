from django.contrib import admin
from .models import Sneakers

@admin.register(Sneakers)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'size','company','category')
    list_display_links = ('id', 'title')
    list_filter = ('size',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 20


# admin.site.register(Sneakers)

# Register your models here.
