

# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    _user = None
    usuario = forms.CharField(label=_(u"User"), widget=forms.TextInput(attrs={'tabindex':1}))
    senha = forms.CharField(label=_(u"Password"), max_length=20,widget=forms.PasswordInput(attrs={'tabindex':2}))

    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)

    def clean_usuario(self):
        return self.cleaned_data['usuario'].lower()

    def clean(self):
        cleaned_data = self.cleaned_data
        if 'usuario' in cleaned_data and 'senha' in cleaned_data:
            self._user = authenticate(username=cleaned_data['usuario'], password=cleaned_data['senha'])
            if not self._user:
                self._errors["usuario"] = ErrorList([_(u"Invalid user or password.")])
        return cleaned_data

    @property
    def user(self):
        return self._user

