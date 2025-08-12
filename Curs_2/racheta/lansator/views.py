from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def zile_pana_la_lansare(request):
    return HttpResponse("Mai sunt 100 zile")

def nume_racheta_view(request):
    return HttpResponse("Numele rachetei este Corina")

def racheta_template_view(request):
    return render(request, "index.html")

from datetime import datetime

luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie",
         "Octombrie", "Noiembrie", "Decembrie"]

def today_view(request):
    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day

    context = {
        'data': f'{day} - {luni[month-1]} - {year}'
    }
    return render(request, "data.html", context)
    return HttpResponse(today)