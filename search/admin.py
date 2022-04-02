from django.contrib import admin
from .models import importkey, importkey_new  
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(importkey)
@admin.register(importkey)
class ImportKeyAdmin(ImportExportModelAdmin):
    # list_display = '_'
    pass
@admin.register(importkey_new)
class ImportKeyAdmin1(ImportExportModelAdmin):
    # list_display = '_'
    pass




