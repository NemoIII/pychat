from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
"""
  Na def home, será renderizado o template home.html, que está no diretório template.
  - def: home
    :param: request
  - def: room
    :param: room
  - def: checkview
    :param: 
"""
def home(request):
  return render(request, 'home.html')

def room(request, room):
  return render(request, 'room.html')

# Fazer check se o room existe na DB.
def checkview(request):
  room = request.POST['room_name']
  username = request.POST['username']

  if Room.objects.filter(name=room).exists(): # Se a room name existe
    return redirect('/'+room+'/?username='+username) # Redirecionamos para o room
  else:
    new_room = Room.objects.create(name=room)
    new_room.save() # Assim é salvo o novo room na DB.
    return redirect('/'+room+'/?username='+username) # Redirecionamos para o room