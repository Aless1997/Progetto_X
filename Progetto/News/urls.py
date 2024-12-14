from django.urls import path
from News.views import rda,insertRda,RdaUpdateView,rdaDetail,export_rda,aziende,ordini,export_fornitore,FornitoreUpdate,registrazione,insertFornitore,fornitore_detail,fornitore_list,export_ordini,area_personale,cambia_utente,OrdiniUpdateViews,ordiniDetail,insertOrdine,export_utenti,insertArticoli,MagazzinoUpdateViews,export_articolo, magazzino_detail,magazzino, export_aziende ,utenti,insertAzienda, insertUtente, utente_detail,azienda_detail,AziendaUpdateViews, UtenteUpdateViews   
from django.contrib.auth import views as auth_views

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
    #Url x ordini
    path('ordini/',ordini, name='ordini'),
    path('insert-ordine/',insertOrdine, name='insert-ordine'),
    path('ordini/<int:pk>', ordiniDetail, name='ordini-detail'),
    path('ordini/<int:pk>/edit',OrdiniUpdateViews.as_view(), name='update-ordini'),
    path('export-ordini/',export_ordini, name='export_products_csv_ord'),

    path('CreaUser/',registrazione, name='registrazione'),
    path('cambia_utente/', cambia_utente, name='cambia_utente'),
    path('area_personale/', area_personale, name='area_personale'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', area_personale, name='area_personale'),
    #fornitore
    path('FornitoreList', fornitore_list, name='fornitore_list'),
    path('FornitoreDetail/<int:pk>/',fornitore_detail, name='fornitore-detail'),
    path('InsertFornitore/', insertFornitore, name='insert-fornitore'),
    path('fornitore/<int:pk>/edit', FornitoreUpdate.as_view(), name="fornitore-update"),
    path('export-fornitori/',export_fornitore, name='export-fornitore'),
    #rda
    path('RdaList/', rda, name='Rda_List'),
    path('RdaExport/', export_rda, name='Export_Rda'),
    path('InsertRda/', insertRda, name='Insert_Rda'),
    path('RdaDetail/<int:pk>/',rdaDetail, name='rda_detail'),
    path('RdaUpdate/<int:pk>/edit/', RdaUpdateView.as_view(), name='rda-update')
]


#next_page='registration/logged_out.html'