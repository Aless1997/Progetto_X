from News.models import *
from django.forms import ModelForm

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