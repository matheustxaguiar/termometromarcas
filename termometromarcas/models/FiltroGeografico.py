from django.db import models

from termometromarcas.models.Filtro import Filtro


class FiltroGeografico(Filtro):
    tipo = models.CharField('Tipo', max_length=30, null=False, blank=False)
    valor = models.CharField('Valor', max_length=30, null=False, blank=False)

    def __str__(self):
        return self.tipo