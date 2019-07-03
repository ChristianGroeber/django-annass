from django.shortcuts import render
from .models import UeberMich, Kontakt


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def ueber_mich(request):
    ueber_mich = UeberMich.objects.get(pk=1)
    return render(request, 'pages/ueber-mich.html', {'ueber_mich': ueber_mich})


def kontakt(request):
    kontakt = Kontakt.objects.get(pk=1)
    return render(request, 'pages/kontakt.html', {'kontakt': kontakt})
