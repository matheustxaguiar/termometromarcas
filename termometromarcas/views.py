from django.shortcuts import render
# from models import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def perform_create(self, serializer):
            serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
