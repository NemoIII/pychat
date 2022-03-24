from django.contrib import admin
from .models import Room, Message

"""
  Estamos a fazer o import desses dois models criados para o admin,
  pois quando for acessado pelo localhost:8000/admin, poderá ser visto e manipulado por lá de maneira mais simples.
"""
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)