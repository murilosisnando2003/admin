from django.db import models
import re
class OracleBlobField(models.Field):
    def get_placeholder(self, value, connection):
        return "UTL_RAW.CAST_TO_RAW(%s)"

    def db_type(self):
        return 'blob'

class Varchar7Fk(models.ForeignKey):
    def db_type(self, connection):
        return 'VARCHAR2(7)'

class Varchar3Fk(models.ForeignKey):
    def db_type(self, connection):
        return 'VARCHAR2(3)'


class view_alertaremanufatura(models.Model):
    class Meta:
        db_table = 'view_alertaremanufatura'
    empresa = models.CharField(max_length=20)
    chave = models.IntegerField(primary_key=True)
    nota = models.CharField(max_length=10, blank=True)
    emissao = models.DateField(null=True, blank=True)
    entrada = models.DateField(null=True, blank=True)
    entidade = models.TextField(blank=True)
    aviso = models.CharField(max_length=10, blank=True)
