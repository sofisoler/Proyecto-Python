from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=15, label='Nombre de usuario')
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, label='Teléfono')
    birth_date = forms.DateField(label='Fecha de nacimiento')
    profile_picture = forms.ImageField(label='Foto de perfil')
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_picture']