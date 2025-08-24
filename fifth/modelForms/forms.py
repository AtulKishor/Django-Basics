from django import forms
from modelForms.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'