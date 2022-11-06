from django.shortcuts import render
# from models import *
from rest_framework import viewsets

from termometromarcas.models import (FiltroGeografico, FiltroTempo, Pesquisa,
                                     Tweet, Usuario, UsuarioJuridico)
from termometromarcas.models.UsuarioFisico import UsuarioFisico

from .serializers import (FisicoSerializer, GeograficoSerializer,
                          JuridicoSerializer, PesquisaSerializer,
                          TempoSerializer, TweetSerializer, UsuarioSerializer)


# Create your views here.
class PesquisaViewSet(viewsets.ModelViewSet):
    serializer_class = PesquisaSerializer
    queryset = Pesquisa.Pesquisa.objects.all()


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.Tweet.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.Usuario.objects.all()


class TempoViewSet(viewsets.ModelViewSet):
    serializer_class = TempoSerializer
    queryset = FiltroTempo.FiltroTempo.objects.all()


class GeograficoViewSet(viewsets.ModelViewSet):
    serializer_class = GeograficoSerializer
    queryset = FiltroGeografico.FiltroGeografico.objects.all()

    
class FisicoViewSet(viewsets.ModelViewSet):
    serializer_class = FisicoSerializer
    queryset = UsuarioFisico.objects.all()

    
class JuridicoViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicoSerializer
    queryset = UsuarioJuridico.UsuarioJuridico.objects.all()
