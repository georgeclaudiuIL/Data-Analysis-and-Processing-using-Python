"""
URL configuration for racheta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lansator.views import zile_pana_la_lansare, nume_racheta_view, racheta_template_view, \
today_view
from culori.views import random_color_view, hex_color_view, rgb_color_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lansare/', zile_pana_la_lansare),
    path('nume/', nume_racheta_view),
    path('', racheta_template_view),
    path('azi/', today_view),
    path('culori', random_color_view),
    path('culoare/<hex>', hex_color_view),
    path('culoare/<r>/<g>/<b>', rgb_color_view),
]
