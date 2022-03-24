from django.db import models
from datetime import datetime

"""
  Aqui será criado as tabelas e colunas no DB
  Abaixo temos as tabelas:
  - class: Room
    :param: name

  - class: Message
    :param: value
"""
# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=1000)

class Message(models.Model):
  value = models.TextField(max_length=10000) # A quantidade de caracteres no TextField pode ser qualquer um.
  date = models.DateTimeField(default=datetime.now, blank=True)
  room = models.CharField(max_length=500)
  user = models.CharField(max_length=500) # Pode ser usado o método de FK, mas nesse caso não será usado.
