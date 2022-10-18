from dataclasses import dataclass
from unittest.util import _MAX_LENGTH

from django.db import models


# Create your models here.
class Tweet(models.Model):
    conteudo = models.CharField('Conteudo', max_length=280, null=False, blank=False)
    data = models.DateField('Data', null=False, blank=False)
    like = models.IntegerField('Like', null=False, blank=False)
    visualizacao = models.IntegerField('Visualizacao', null=False, blank=False)
    retweet = models.IntegerField('Retweet', null=False, blank=False)
    usuario = models.CharField('Usuario', max_length=50, null=False, blank=False)
    polaridade = models.IntegerField('Polaridade', null=False, blank=False)
    subjetividade = models.IntegerField('Subjetividade', null=False, blank=False)


class Pesquisa(models.Model):
    data = models.DateTimeField('Data', null=False, blank=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    termo = models.CharField('Pesquisa', max_length=30, null=False, blank=False)
    tweet = models.ManyToManyField(Tweet, null=False, blank=False)


# class Filtro(models.Model):
#     nome = models.CharField('Nome', max_length=20, null=False, blank=False)

#     class Meta: 
#         abstract = False


class Tempo(models.Model):
    # objects = Filtro()
    dataInicial = models.DateField('Data Inicial', null=False, blank=False)
    dataFinal = models.DateField('Data Final', null=False, blank=False)


class Geografico(models.Model):
    # objects = Filtro()
    tipo = models.CharField('Tipo', max_length=30, null=False, blank=False)
    valor = models.CharField('Valor', max_length=30, null=False, blank=False)


class Usuario(models.Model):
    usuario = models.CharField('Usuario', max_length=30, null=False, blank=False)
    email = models.CharField('Email', max_length=50, null=False, blank=False)
    senha = models.CharField('Senha', max_length=30, null=False, blank=False)

    
class Fisico(models.Model):
    cpf = models.IntegerField('CPF', null=False, blank=False)


class Juridico(models.Model):
    cnpj = models.BigIntegerField('CPNJ', null=False, blank=False)
