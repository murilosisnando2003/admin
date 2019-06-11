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

def validate_CNPJ(value):
    """
    Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a
    group of 14 characters.
    :type value: object
    """
    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) > 14:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value

class Clientes(models.Model):
    Status_CHOICES =[('Ativo','Ativo'),('Desativado','Desativado')]

    name = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    emailcontato = models.EmailField(blank=True)
    emailfinanceiro = models.EmailField(blank=True)
    tipo = models.CharField(choices=Status_CHOICES,default='Ativo',max_length=50)
    datacadastro = models.DateField(auto_now=True)
    location = models.CharField(max_length=200, blank=True)
    cnpj = models.CharField(unique=True, max_length=14, validators=[validate_CNPJ])



class Apolo(models.Model):
    class Meta:
        db_table = 'apolo'
    apolover = models.CharField(max_length=7, unique=True)
    apolodatahora = models.DateField(null=True, blank=True)
    apoloalter = models.CharField(max_length=20, blank=True)
    apolomp135 = models.CharField(max_length=10, blank=True)
    

    
