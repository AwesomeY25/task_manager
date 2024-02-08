from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_fname', 'user_lname', 'user_email', 'user_password', 'user_account_type']
        widgets = {
            'user_fname': forms.TextInput(attrs={'class': 'form-control'}),
            'user_lname': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'user_account_type': forms.Select(attrs={'class': 'form-control'})
        }
