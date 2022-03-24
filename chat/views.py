from django.shortcuts import render

# Create your views here.
"""
  Na def home, será renderizado o template home.html, que está no diretório template.
  - def: home
    :param: request
  - def: room
    :param: room
"""
def home(request):
  return render(request, 'home.html')

def room(request):
  return render(request, 'room.html')