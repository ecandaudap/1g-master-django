from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def get_koder(request, id):
    koders = [
        {"id": 1, "name": "Benjamin", "generation": "ig", "bootcamp": "Python"},
        {"id": 2, "name": "Luis", "generation": "ig", "bootcamp": "Python"}
    ]

    founded_koder  = [koder for koder in koders if koder.id == id]
    print("Founded koder --->>>", founded_koder[0])

    return HttpResponse(f"Founded koder --->>> {founded_koder}")

def list_koders(request):
    context = {
        "bootcamp":{"name": "Python", "module": "Django"},
        "koders" : [
            {"name": "Benjamin", "generation": "ig", "bootcamp": "Python", "is_active": True},
            {"name": "Luis", "generation": "ig", "bootcamp": "Python", "is_active": True},
            {"name": "Enrique", "generation": "ig", "bootcamp": "Python", "is_active": False}
        ],
    }

    template = loader.get_template("bootcamp/templates/list_koders.html")
    return HttpResponse(template.render(context, request))
