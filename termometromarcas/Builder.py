# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
import re
from rest_framework import serializers
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
        regex = r'\b[A-Za-z0-9 ]{2,}\b'
        if(re.fullmatch(regex, usuario)):
            return usuario
 
        else:
            raise serializers.ValidationError("O usuário não pode ter caracteres especiais")
       

    def validar_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
 
        else:
            raise serializers.ValidationError("Email invalido")

    def validar_senha(self, senha):
        l, u, p, d = 0, 0, 0, 0
        s = senha
        if (len(s) >= 8):
            for i in s:
        
                # counting lowercase alphabets
                if (i.islower()):
                    l+=1           
        
                # counting uppercase alphabets
                if (i.isupper()):
                    u+=1           
        
                # counting digits
                if (i.isdigit()):
                    d+=1           
        
                # counting the mentioned special characters
                if(i=='@'or i=='$' or i=='_'):
                    p+=1          
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
            print("Valid Password")
        else:
            raise serializers.ValidationError("a senha deve conter no mínimo 8 caracteres, sendo eles: números, letras maiúsculas, minúsculas e caracteres especiais")

        return self

    def get_result(self):
        # ???
        return self

class Director():
    # "The Director, building a complex representation."

    @staticmethod
    def construct(instancia):
        usuariobuilder = UsuarioBuilder()
        usuariobuilder.validar_usuario(instancia.usuario)
        usuariobuilder.validar_email(instancia.email)
        usuariobuilder.validar_senha(instancia.senha)
