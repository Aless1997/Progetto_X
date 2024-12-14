from django.contrib import admin
from News.models import Azienda, Utente,Ordine,Magazzino, Fornitore, Rda

admin.site.register(Azienda)
admin.site.register(Utente)
admin.site.register(Ordine)
admin.site.register(Magazzino)
admin.site.register(Fornitore)
admin.site.register(Rda)