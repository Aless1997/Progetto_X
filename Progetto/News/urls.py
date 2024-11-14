from django.urls import path
from News.views import aziende, utenti,insertAzienda, insertUtente, azienda_detail,AziendaUpdateViews, UtenteUpdateViews   

urlpatterns = [
    path('Aziende/', aziende, name='aziende'),
    path('Utenti/', utenti, name='utenti'),
    path('InsertAzienda/', insertAzienda, name='insert-azienda'),
    path('InsertUtente/', insertUtente, name='insert-utente'),
    path('ModificaAzienda/<int:pk>/edit/', AziendaUpdateViews.as_view(), name='update-azienda'),
    path('ModificaUtente/<int:pk>/edit/', UtenteUpdateViews.as_view(), name='update-utente'),
    path('azienda/<int:pk>/', azienda_detail, name='azienda-detail'),
    
]