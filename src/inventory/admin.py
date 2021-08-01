from django.contrib import admin
from .models import Device,Laptop,Desktop,Mobile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Desktop,Laptop,Mobile)
class ViewAdmin(ImportExportModelAdmin):
    
    pass