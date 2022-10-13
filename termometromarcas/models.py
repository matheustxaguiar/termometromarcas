from dataclasses import dataclass
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Pesquisa(models.Model):
    data = models.DateField()
    quantidade = models.IntegerField()
    termo = models.CharField(max_length=255)
