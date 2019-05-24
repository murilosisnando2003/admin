from django.db import models

# Create your models here.

class Empresa(models.Model):

    Status_CHOICES =[('Ativo','Ativo'),('Desativado','Desativado')]
    Nome = models.CharField(max_length=150)
    Tipo = models.CharField(choices=Status_CHOICES,default='Ativo',max_length=50)

    def __str__(self):
        return self.Nome


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)