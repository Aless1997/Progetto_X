from django.contrib import admin
from News.models import Azienda, Utente,Ordine,Magazzino

admin.site.register(Azienda)
admin.site.register(Utente)
admin.site.register(Ordine)
admin.site.register(Magazzino)