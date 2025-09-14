from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'founded', 'stadium', 'coach']
        labels = {
            'name': 'Nombre',
            'city': 'Ciudad',
            'founded': 'Año de Fundación',
            'stadium': 'Estadio',
            'coach': 'Entrenador',
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electrónico')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
