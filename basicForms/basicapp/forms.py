from django import forms
from django.core import validators

def check_a(value):
    if 'a' not in value.lower():
        raise forms.ValidationError("Name should have letter A")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter email again: ")
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, 
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data =  super().clean()
        if all_clean_data['email']!=all_clean_data['verify_email']:
            raise forms.ValidationError("email and verify_email doesen't match!")