from django.db import models

from termometromarcas.models import Filtro, Tweet


class Pesquisa(models.Model):
    data = models.DateField('Data', null=False, blank=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    termo = models.CharField('Pesquisa', max_length=30, null=False, blank=False)
    tweet = models.ManyToManyField(Tweet.Tweet)
    filtro = models.ManyToManyField(Filtro.Filtro)

    def __str__(self):
        return self.termo