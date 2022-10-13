from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PesquisaSerializer
from .models import Pesquisa


# Create your views here.
class PesquisaViewSet(viewsets.ModelViewSet):
    serializer_class = PesquisaSerializer
    queryset = Pesquisa.objects.all()