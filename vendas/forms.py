# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _
from .models import Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'birth_date', 'location']
