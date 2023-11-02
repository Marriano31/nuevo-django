from django.urls import path
from inicio.views import inicio, paletas, crear_paleta, raqueta, crear_raqueta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),           #paletas/ para poder acceder
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    
    path('raqueta/', raqueta, name='raquetas'),           #paletas/ para poder acceder
    path('raqueta/crear/', crear_raqueta, name='crear_raqueta')
]
