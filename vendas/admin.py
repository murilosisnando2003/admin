from django.contrib import admin
from .models import Empresa,Person,Classificacao
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Classificacao)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
