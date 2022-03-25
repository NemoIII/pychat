from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
"""
  Na def home, será renderizado o template home.html, que está no diretório template.
  - def: home
    :param: request
  - def: room
    :param: request
    :param: room
  - def: checkview
    :param: request
  - def: send
    :param: request
  - def: getMessages
    :param: request
    :param: room
"""
def home(request):
  return render(request, 'home.html')

def room(request, room):
  username = request.GET.get('username')
  room_details = Room.objects.get(name=room)
  return render(request, 'room.html',{
    'username': username,
    'room': room,
    'room_details': room_details,
  })

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

def send(request):
  message = request.POST['message']
  username = request.POST['username']
  room_id = request.POST['room_id']
  
  new_message = Message.objects.create(
    value=message, user=username, room=room_id
  )
  new_message.save()
  return HttpResponse("Hi, message sent successfully!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})