from django.urls import path
from News.views import aziende, utenti,insertAzienda, insertUtente

urlpatterns = [
    path('Aziende/', aziende, name='aziende'),
    path('Utenti/', utenti, name='aziende'),
    path('InsertAzienda/', insertAzienda, name='aziende'),
    path('InsertUtente/', insertUtente, name='aziende'),
]