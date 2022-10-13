from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Pesquisa


class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa
        fields = '__all__'