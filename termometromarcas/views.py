from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


# Create your views here.
class PesquisaViewSet(viewsets.ModelViewSet):
    serializer_class = PesquisaSerializer
    queryset = Pesquisa.objects.all()


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TempoViewSet(viewsets.ModelViewSet):
    serializer_class = TempoSerializer
    queryset = Tempo.objects.all()


class GeograficoViewSet(viewsets.ModelViewSet):
    serializer_class = GeograficoSerializer
    queryset = Geografico.objects.all()

    
class FisicoViewSet(viewsets.ModelViewSet):
    serializer_class = FisicoSerializer
    queryset = Fisico.objects.all()

    
class JuridicoViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicoSerializer
    queryset = Juridico.objects.all()
