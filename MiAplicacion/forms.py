# MiAplicacion/forms.py
from django import forms
from .models import Autor, Libro, Pelicula, Editorial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class BuscarAutorForm(forms.Form):
    nombre = forms.CharField(required=False)  # Permite que el campo sea opcional

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'