from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request, response
from News.models import Azienda, Utente
from News.forms import InsertAzienda, InsertUtente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

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