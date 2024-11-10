from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request, response
from News.models import Azienda, Utente
from News.forms import InsertAzienda, InsertUtente

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