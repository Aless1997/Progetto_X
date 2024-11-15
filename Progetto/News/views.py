from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request, response
from News.models import Azienda, Utente, Magazzino, Ordine
from News.forms import InsertAzienda, InsertUtente, InsertArticoli
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
import pandas as pd

def aziende(request):
    azienda = Azienda.objects.all()
    context = {
        'azienda' : azienda,
    }

    return render(request, 'News/Aziende.html', context)

def utenti(request):
    utente = Utente.objects.all()
    context = {
        'utente' : utente,
    }

    return render(request, 'News/Utente.html', context)

def insertAzienda(request):
    if request.method == 'POST':
        form = InsertAzienda(request.POST)
        if form.is_valid():
            form.save()
    form = InsertAzienda()
    context = {"form":form}
    return render(request, 'News/InsertAzienda.html', context)

def insertUtente(request):
    if request.method == 'POST':
        form = InsertUtente(request.POST)
        if form.is_valid():
            form.save()
    form = InsertUtente()
    context = {"form":form}
    return render(request, 'News/InsertUtente.html', context)

class AziendaUpdateViews(UpdateView):
    model = Azienda
    form_class = InsertAzienda
    template_name = 'News/InsertAzienda.html'
    success_url = reverse_lazy('aziende')

class UtenteUpdateViews(UpdateView):
    model = Utente              
    form_class = InsertUtente
    template_name = 'News/InsertUtente.html'
    success_url = reverse_lazy('utenti')


def azienda_detail(request, pk):
    azienda = get_object_or_404(Azienda, pk=pk)
    context = {
        'azienda': azienda,
    }
    return render(request, 'News/AziendaDetail.html', context)

def utente_detail(request, pk):
    utente = get_object_or_404(Utente, pk=pk)
    context = {
        'utente': utente,
    }
    return render(request, 'News/UtenteDetail.html', context)

def export_utenti(request):
    utenti = Utente.objects.all().values()
    df = pd.DataFrame(utenti)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="utenti.csv"'
    df.to_csv(path_or_buf=response, index=False)
    
    return response

def export_aziende(request):
    aziende = Azienda.objects.all().values()
    df = pd.DataFrame(aziende)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aziende.csv"'
    df.to_csv(path_or_buf=response, index=False)
    
    return response

#Gestione ordini + magazzino

def magazzino(request):
    magazzino = Magazzino.objects.all()
    context = {
        'magazzino':magazzino,
    }
    return render(request, 'News/MagazzinoList.html', context)

def magazzino_detail(request, pk):
    magazzino = get_object_or_404(Magazzino, pk=pk)
    context = {
        'magazzino': magazzino,
    }
    return render(request, 'News/MagazzinoDetail.html', context)

class MagazzinoUpdateViews(UpdateView):
    model = Magazzino              
    form_class = InsertArticoli
    template_name = 'News/InsertArticoli.html'
    success_url = reverse_lazy('magazzino')

def export_articolo(request):
    articoli = Magazzino.objects.all().values()
    df = pd.DataFrame(articoli)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="articoli.csv"'
    df.to_csv(path_or_buf=response, index=False)
    
    return response

def insertArticoli(request):
    if request.method == 'POST':
        form = InsertArticoli(request.POST)
        if form.is_valid():
            form.save()
    form = InsertArticoli()
    context = {"form":form}
    return render(request, 'News/InsertArticoli.html', context)