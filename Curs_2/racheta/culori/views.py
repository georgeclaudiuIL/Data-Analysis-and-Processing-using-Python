from django.shortcuts import render

# Create your views here.

import numpy as np

def random_color_view(request):
    culori_rgb = np.random.randint(0,255, 3)
    context = {
        "rosu" : culori_rgb[0],
        "verde" : culori_rgb[1],
        "albastru" : culori_rgb[2],
    }
    return render(request, 'culoare_random.html', context)

def hex_color_view(request, hex):
    context = {
        'culoare_hex': f"#{hex}"
    }
    return render(request, "hex_color.html", context)

def rgb_color_view(request, r, g, b):
    context = {
        'culoare_hex': f'rgb({r}, {g}, {b})'
    }
    return render(request, "hex_color.html", context)