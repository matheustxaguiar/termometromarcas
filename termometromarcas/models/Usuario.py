from django.db import models

from termometromarcas.models import Pesquisa


class Usuario(models.Model):
    usuario = models.CharField('Usuario', max_length=30, null=False, blank=False)
    email = models.CharField('Email', max_length=50, null=False, blank=False)
    senha = models.CharField('Senha', max_length=30, null=False, blank=False)
    pesquisas = models.ManyToManyField(Pesquisa.Pesquisa, null=True, blank=True)

    def __str__(self):
        return self.email
    
    def setPesquisas(self, pesquisas):
        self.pesquisas = pesquisas
