from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import Pesquisa, Tweet


class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa
        fields = '__all__'
    
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
