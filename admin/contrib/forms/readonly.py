from django.forms import ModelForm
from django import forms

class ReadonlyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReadonlyForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            for f in self.fields:
                if type(self.fields[f].widget) == forms.Select:
                    self.fields[f].widget = forms.TextInput()
                self.fields[f].widget.attrs.update({'readonly': 'readonly'})