from django.forms import ModelForm
from django import forms

class LocalizeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalizeForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            if type(self.fields[f]) == forms.DecimalField:
                self.fields[f].localize = True
                self.fields[f].widget = forms.TextInput()
