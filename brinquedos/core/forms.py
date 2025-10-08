from django import forms
from .models import Brinquedo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrinquedoForm(forms.ModelForm):
    class Meta:
        model = Brinquedo
        fields = ['nome', 'preco', 'quantidade']

class FormRegistro(UserCreationForm):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome de usuário'})
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'class': 'forms-control', 'placeholder': 'Confirme sua senha'})
    )

class Meta:
    model = User
    fields = ['username', 'password1', 'password2']