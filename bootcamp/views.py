from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

from bootcamp.models import Koder

def get_koder(request, id):
    koders = Koder.objects.get(pk=id)

    return HttpResponse(f"Founded koder --->>> {koders}")

from bootcamp.models import Koder


def list_koders(request):
    koders = Koder.objects.all()

    return HttpResponse(koders)

def list_mentors(request):
    context = {
        "mentors": [
            {
                "name": "Benjamin",
                "last_name": "Aguilar",
                "is_active": True
            },
            {
                "name": "Alfredo",
                "last_name": "Altamirano",
                "is_active": True
            },
            {
                "name": "Charles",
                "last_name": "Lopez",
                "is_active": False
            },
        ],
    }




    template = loader.get_template("templates/list_mentors.html")
    return HttpResponse(template.render(context, request))
