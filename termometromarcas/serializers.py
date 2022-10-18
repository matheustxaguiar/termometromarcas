from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import *


class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa
        fields = '__all__'
    
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# class FiltroSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Filtro
#         fields = '__all__'


class TempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tempo
        fields = '__all__'


class GeograficoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geografico
        fields = '__all__'


class FisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisico
        fields = '__all__'


class JuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridico
        fields = '__all__'