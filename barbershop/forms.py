from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Barbershop, Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['barbershop','time','status']

class BarbershopForm(ModelForm):
    class Meta:
        model = Barbershop
        fields = ['Barbershopname','phone','email','area','service']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
