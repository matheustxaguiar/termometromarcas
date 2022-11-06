from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from termometromarcas.models.Usuario import Usuario
from termometromarcas.models.UsuarioObserver import UsuarioObserver

status_usuario = [("ativo", "Ativo"), ("desativado", "Desativado")]


class UsuarioFisico(Usuario):
    cpf = models.IntegerField('CPF', null=False, blank=False)
    status = models.CharField(max_length=255, choices=status_usuario, default="ativo")
    observadores = []

    def __str__(self):
        return self.cpf
    
    def adicionarObservador(self, observador):
        self.observadores.append(observador)

@receiver(pre_save, sender=UsuarioFisico)
def notifyObservers(sender, instance, **kwargs):
    listaObservadores=[]
    ob1 = UsuarioObserver()
    listaObservadores.append(ob1)
    for item in listaObservadores:
        item.update(instance)