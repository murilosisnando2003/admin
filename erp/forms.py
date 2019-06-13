# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _
from .models import view_alertaremanufatura
from django.forms import ModelForm
from django.db.models import Q


class RemanufaturaForm(forms.ModelForm):
    class Meta:
        model = view_alertaremanufatura
        fields = "__all__"

