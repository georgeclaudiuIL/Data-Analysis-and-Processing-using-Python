from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from functools import reduce


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



def factorial_template_view(request, n):
    try:
        n = int(n)
    except:
        return HttpResponse(f"Factorial trebuie sa fie numar >= 0..")
    
    if n<0:
        return HttpResponse(f"Factorial trebuie sa fie >= 0..")
    
    produs = 1 if n < 2 else reduce(lambda x, y: x * y, range(1, n + 1))

    context = {
        "n": n,
        "factorial": produs,
    }
    return render(request, "factorial.html", context)

# def factorial_list_view(request, n):
#     lista_factorial = []
#     try:
#         n = int(n)
#     except:
#         return HttpResponse(f"Factorial trebuie sa fie numar >= 0..")
    
#     if n<0:
#         return HttpResponse(f"Factorial trebuie sa fie >= 0..")
    
#     for i in range(n, -1, -1):
#         lista_factorial.append((i, factorial_template_view(i)))

#     context = {
#         "n": n,
#         "factorial": produs,
#     }
#     return render(request, "factorial.html", context)
