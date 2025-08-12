from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def zile_pana_la_lansare(request):
    return HttpResponse("Mai sunt 100 zile")

def nume_racheta_view(request):
    return HttpResponse("Numele rachetei este Corina")