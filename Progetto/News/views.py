from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, request, response
from News.models import Azienda, Utente, Magazzino, Ordine
from News.forms import InsertAzienda, InsertUtente, InsertArticoli, InsertOrdine,RegsitraForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CambiaUtenteForm

def home(request):
    return render(request, 'News/base.html')    

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

#Gestione magazzino

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

'''----------------------------------------VIEWS X ORDINI----------------------------------------'''

def ordini(request):
    ordini = Ordine.objects.all()
    context = {
        'ordini' : ordini,
    }
    return render(request, 'News/OrdiniList.html', context)


def insertOrdine(request):
    if request.method == 'POST':
        form = InsertOrdine(request.POST)
        if form.is_valid():
            form.save()
    form = InsertOrdine()
    context = {"form":form}
    return render(request, 'News/InsertOrdine.html', context)

def ordiniDetail(request, pk):
    ordini = get_object_or_404(Ordine, pk=pk)
    context = {
        'ordini': ordini,
    }
    return render(request, 'News/OrdiniDetail.html', context)

class OrdiniUpdateViews(UpdateView):
    model = Ordine              
    form_class = InsertOrdine
    template_name = 'News/InsertOrdine.html'
    success_url = reverse_lazy('ordini')

def export_ordini(request):
    ordini = Ordine.objects.all().values()
    df = pd.DataFrame(ordini)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ordini.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response

def registrazione(request):
    if request.method == 'POST':
        form_2 = RegsitraForm(request.POST)
        if form_2.is_valid():
            form_2.save()
            return redirect('utenti') 
        else:
            print(form_2.errors)
    else:
        form_2 = RegsitraForm()
    context = {"form_2" : form_2}
    return render(request, 'News/User.html', context)

@login_required
def cambia_utente(request):
    if request.method == 'POST':
        form = CambiaUtenteForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('area_personale')
    else:
        form = CambiaUtenteForm(instance=request.user)
    return render(request, 'News/cambia_utente.html', {'form': form})

@login_required
def area_personale(request):
    return render(request, 'News/area_personale.html')