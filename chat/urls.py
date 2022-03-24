from django.urls import path
from . import views

"""
  Aqui será chamara as funções que foram criadas em views.
  Colocar um nome não é obrigatório.
"""
urlpatterns = [
  path('', views.home, name="home"),
  path('<str:room>/', views.room, name="room"),
  path('checkview', views.checkview, name="checkview"),
]