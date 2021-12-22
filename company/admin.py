from django.contrib import admin
from .models import Company

@admin.register(Company)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    list_display_links = ('id', 'company_name')
    search_fields = ('company_name',)
    list_per_page = 20


# admin.site.register(Company)



# Register your models here.
