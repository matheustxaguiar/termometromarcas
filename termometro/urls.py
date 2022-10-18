"""termometro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from termometromarcas.views import *

route = routers.DefaultRouter()

route.register('pesquisa', PesquisaViewSet, basename='Pesquisa')
route.register('tweet', TweetViewSet, basename='Tweet')
route.register('usuario', UsuarioViewSet, basename='Usuario')
route.register('geografico', GeograficoViewSet, basename='Geografico')
route.register('tempo', TempoViewSet, basename='Tempo')
route.register('fisico', FisicoViewSet, basename='Fisico')
route.register('juridico', JuridicoViewSet, basename='Juridico')
# route.register('filtro', FiltroViewSet, basename='Juridico')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
