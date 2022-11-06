from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from termometromarcas.Builder import Director
from termometromarcas.models import (FiltroGeografico, FiltroTempo, Pesquisa,
                                     Tweet, UsuarioJuridico)
from termometromarcas.models.Usuario import Usuario
from termometromarcas.models.UsuarioFisico import UsuarioFisico


class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa.Pesquisa
        fields = '__all__'
    
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet.Tweet
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        Director.construct(instance)
        return instance

class TempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiltroTempo.FiltroTempo
        fields = '__all__'


class GeograficoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiltroGeografico.FiltroGeografico
        fields = '__all__'


class FisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioFisico
        fields = '__all__'


class JuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioJuridico.UsuarioJuridico
        fields = '__all__'