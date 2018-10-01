from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', min_length=3, max_length=50)
    password = forms.CharField(label='Пароль', min_length=5, max_length=50, widget=forms.PasswordInput())

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


class RegistrationForm(forms.ModelForm):
    password_1 = forms.CharField(label='Пароль', min_length=5, max_length=50, widget=forms.PasswordInput())
    password_2 = forms.CharField(label='Повторите пароль', min_length=5, max_length=50, widget=forms.PasswordInput())
    
    password_1.widget.attrs.update({'class': 'form-control'})
    password_2.widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_password_2(self):
        if self.cleaned_data.get('password_1') != self.cleaned_data.get('password_2'):
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data.get('password_2')
    
