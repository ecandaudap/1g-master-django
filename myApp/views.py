from django.shortcuts import render

# Importar HttpResponse
from django.http import HttpResponse
from django.template import loader


def bienvenida(request):
    # Responder
    return HttpResponse("Bienvenida")

def despedida(request):
    return HttpResponse("Despedida")

def saludo(request):
    return HttpResponse("Saludando a los Koders")

def saludar_con_nombre(request, nombre):
    context = {"nombre": nombre} # Va a servir para pasarle info al template
    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))

def saludar_con_nombre2(request, nombre, type):
    context = {"nombre": nombre, "type": type} # Va a servir para pasarle info al template
    template = loader.get_template("base2.html")
    return HttpResponse(template.render(context, request))


def saludar_tipo(request, type):
    if type == "mentor":
        return HttpResponse(f'Hello {type} here are your classes')
    elif type == "koder":
        return HttpResponse(f'Hello {type} welcome to kodemia')
    else:
        return HttpResponse(f'You are not welcome here')
    
