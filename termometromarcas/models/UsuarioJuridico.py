from django.db import models

from termometromarcas.models.Usuario import Usuario


class UsuarioJuridico(Usuario):
    cnpj = models.BigIntegerField('CPNJ', null=False, blank=False)