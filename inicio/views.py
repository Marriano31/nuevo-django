from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from inicio.models import Paleta
from inicio.models import raqueta

def inicio (request):
    
    #template = loader.get_template('inicio.html')
    #template_renderizado=template.render({})
    
    # return HttpResponse(template_renderizado)

# Create your views here.

    return render( request , 'inicio/paletas.html', {})

def paletas(request):
 
    return render(request, 'inicio/paletas.html')

def crear_paleta(request):
    
    if request.method == 'POST':
        marca =request.POST.get('marca')
        descripcion =request.POST.get('descripcion')
        anio =request.POST.get('año')
        
        paleta = Paleta(marca = marca, descripcion = descripcion, anio = anio)
        
        paleta.save()
        
        return render(request, 'inicio/crear_paleta.html', {})    
    
    
    def crear_raqueta(request):
    
     if request.method == 'POST':
        marca =request.POST.get('marca')
        descripcion =request.POST.get('descripcion')
        anio =request.POST.get('año')
        
        raqueta = raqueta(marca = marca, descripcion = descripcion, anio = anio)
        
        raqueta.save()
        
        return render(request, 'inicio/crear_raqueta.html', {}) 
    # print('===========')
    # print('GET')
    # print(request.GET)
    # print('===========')
    # print('POST')
    # print(request.POST)
    # return render(request, 'inicio/crear_paleta.html', {}