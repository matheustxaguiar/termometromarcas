from django.shortcuts import render
from rest_framework import viewsets

from .models import Pesquisa, Tweet
from .serializers import PesquisaSerializer, TweetSerializer


# Create your views here.
class PesquisaViewSet(viewsets.ModelViewSet):
    serializer_class = PesquisaSerializer
    queryset = Pesquisa.objects.all()


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
