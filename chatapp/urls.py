from django.contrib import admin
from django.urls import path, include


'''
	Após fazer o import do "include", podemos incluir o urls do app chat no núcleo do projeto.
	Através disso ele irá renderizar tudo que foi feito no app.
'''
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('chat.urls')),
]
