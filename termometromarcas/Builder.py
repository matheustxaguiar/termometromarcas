# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"Builder Concept Sample Code"
from abc import ABCMeta, abstractmethod

from .models.Usuario import Usuario


class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def validar_usuario():
        print("validar_usuario")

    @staticmethod
    @abstractmethod
    def validar_email():
        print("validar_email")

    @staticmethod
    @abstractmethod
    def validar_senha():
        print("validar_senha")

    @staticmethod
    @abstractmethod
    def get_result():
        print("get_result")

class UsuarioBuilder(IBuilder):
    # "The Concrete Builder."

    def validar_usuario(self, usuario):
        print(usuario)
        #self.product.parts.append('a')
        return self

    def validar_email(self, email):
        print(email)
        #self.product.parts.append('b')
        return self

    def validar_senha(self, senha):
        print(senha)
        #self.product.parts.append('c')
        return self

    def get_result(self):
        print("mds q sofrimento")


class Director():
    # "The Director, building a complex representation."

    @staticmethod
    def construct(instancia):
        usuariobuilder = UsuarioBuilder()
        usuariobuilder.validar_usuario(instancia.usuario)
        usuariobuilder.validar_email(instancia.email)
        usuariobuilder.validar_senha(instancia.senha)
