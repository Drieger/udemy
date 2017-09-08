from django import forms
from django.core import validators

from basicapp.models import User

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Email Again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        verify_email = all_cleaned_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Emails do not match")



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
