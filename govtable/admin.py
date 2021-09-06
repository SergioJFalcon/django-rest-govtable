from django.contrib import admin
from .models import GovTable

class GovTableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'ZipCode', 'Email')

# Register your models here.
admin.site.register(GovTable, GovTableAdmin)