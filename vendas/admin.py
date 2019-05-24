from django.contrib import admin
from .models import Empresa,Person
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Empresa)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
