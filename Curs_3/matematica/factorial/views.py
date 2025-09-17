from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def factorial_view(request, n):
    try:
        n = int(n)
    except:
        return HttpResponse(f"Factorial trebuie sa fie numar >= 0..")
    
    if n<0:
        return HttpResponse(f"Factorial trebuie sa fie >= 0..")
    
    factorial = 1
    raspuns = f"{n}! = "
    scadere = 0
    for i in range(n,0,-1):
        factorial = factorial*i
        raspuns = raspuns + f"{n-scadere} * "
        scadere += 1
    raspuns = raspuns[:-2]
    raspuns = raspuns + f"= {factorial}"
    return HttpResponse(raspuns)

