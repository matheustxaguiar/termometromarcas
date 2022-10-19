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


class Filtro(models.Model):
    def __str__(self):
        return 'filtro'

class Tempo(Filtro):
    dataInicial = models.DateField('Data Inicial', null=False, blank=False)
    dataFinal = models.DateField('Data Final', null=False, blank=False)

    def __str__(self):
        return self.dataInicial

class Geografico(Filtro):
    tipo = models.CharField('Tipo', max_length=30, null=False, blank=False)
    valor = models.CharField('Valor', max_length=30, null=False, blank=False)

    def __str__(self):
        return self.tipo

    
class Pesquisa(models.Model):
    data = models.DateField('Data', null=False, blank=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    termo = models.CharField('Pesquisa', max_length=30, null=False, blank=False)
    tweet = models.ManyToManyField(Tweet)
    filtro = models.ManyToManyField(Filtro)

    def __str__(self):
        return self.termo


class Usuario(models.Model):
    usuario = models.CharField('Usuario', max_length=30, null=False, blank=False)
    email = models.CharField('Email', max_length=50, null=False, blank=False)
    senha = models.CharField('Senha', max_length=30, null=False, blank=False)
    pesquisas = models.ManyToManyField(Pesquisa, null=True, blank=True)

    def __str__(self):
        return self.usuario

    
class Fisico(Usuario):
    cpf = models.IntegerField('CPF', null=False, blank=False)


class Juridico(Usuario):
    cnpj = models.BigIntegerField('CPNJ', null=False, blank=False)
