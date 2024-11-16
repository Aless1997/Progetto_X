from News.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InsertAzienda(ModelForm):
    class Meta():
        model = Azienda
        fields = "__all__"

class InsertUtente(ModelForm):
    class Meta():
        model = Utente
        fields = "__all__"

class InsertArticoli(ModelForm):
    class Meta:
        model = Magazzino
        fields = '__all__'

class InsertOrdine(ModelForm):
    class Meta():
        model=Ordine
        fields = '__all__'

class RegsitraForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

from django import forms
from django.contrib.auth.models import User

class CambiaUtenteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Aggiungi altri campi se necessario