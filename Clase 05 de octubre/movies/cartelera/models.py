from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class movie (models.Model) :
    name = models.CharField(max_length = 100)
    comentario = models.TextFiel

class Director (models.Model):
    