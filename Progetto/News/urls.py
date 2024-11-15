from django.urls import path
from News.views import aziende, export_utenti,insertArticoli,MagazzinoUpdateViews,export_articolo, magazzino_detail,magazzino, export_aziende ,utenti,insertAzienda, insertUtente, utente_detail,azienda_detail,AziendaUpdateViews, UtenteUpdateViews   

urlpatterns = [
    path('Aziende/', aziende, name='aziende'),
    path('Utenti/', utenti, name='utenti'),
    path('InsertAzienda/', insertAzienda, name='insert-azienda'),
    path('InsertUtente/', insertUtente, name='insert-utente'),
    path('ModificaAzienda/<int:pk>/edit/', AziendaUpdateViews.as_view(), name='update-azienda'),
    path('ModificaUtente/<int:pk>/edit/', UtenteUpdateViews.as_view(), name='update-utente'),
    path('azienda/<int:pk>/', azienda_detail, name='azienda-detail'),
    path('utente/<int:pk>/',utente_detail, name='utente-detail'),
    path('export/csv/', export_utenti, name='export_products_csv'),
    path('export/csv/az', export_aziende, name='export_products_csv_az'),
    
    path('export/csv/art', export_articolo, name='export_products_csv_art'),  
    path('magazzino/', magazzino, name='magazzino'),
    path('magazzino/<int:pk>/', magazzino_detail, name='magazzino-detail'),
    path('insert-articolo/', insertArticoli, name='insert-articolo'),
    path('update-articolo/<int:pk>/', MagazzinoUpdateViews.as_view(), name='update-articolo'),
    path('export-articolo/', export_articolo, name='export-articolo'),


]

