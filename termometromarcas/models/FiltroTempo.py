from django.db import models

from termometromarcas.models.Filtro import Filtro


class FiltroTempo(Filtro):
    dataInicial = models.DateField('Data Inicial', null=False, blank=False)
    dataFinal = models.DateField('Data Final', null=False, blank=False)

    def __str__(self):
        return self.dataInicial