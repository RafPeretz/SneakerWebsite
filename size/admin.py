from django.contrib import admin
from .models import Size


@admin.register(Size)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'size_us','size_uk','size_eu')
    list_display_links = ('id', 'size_us')
    search_fields = ('size_us',)
    list_per_page = 20

# admin.site.register(Size)

# Register your models here.
