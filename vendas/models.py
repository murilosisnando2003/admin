from django.db import models
from django.urls import reverse

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


class Classificacao(models.Model):
    codigo = models.CharField(max_length=15,unique=True)
    descricao = models.TextField()


    def __unicode__(self):
        return (self.codigo)

    def get_absolute_url(self):
        return reverse('edit_classificacao_pk', kwargs={'obj': self.pk})

class Post(models.Model):
    title = models.CharField(max_length=120, help_text='title of message.')
    message = models.TextField(help_text="what's on your mind ...")
 
    def __str__(self):
        return self.title