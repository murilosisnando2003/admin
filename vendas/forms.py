# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _
from .models import Person,Classificacao,Post
from django.forms import ModelForm
from django.db.models import Q

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'birth_date', 'location']


class FormQueryClassificacao(forms.Form):
    q = forms.CharField(required=False)

    def query(self):
        itens = Classificacao.objects.all()
        q = self.cleaned_data['q']
        if self.cleaned_data['q']:
           itens = itens.filter(Q(codigo__icontains=q) | Q(descricao__icontains=q) )
        return itens


class FormClassificacao(forms.ModelForm):
    class Meta:
        model = Classificacao
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

