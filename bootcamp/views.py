from django.shortcuts import render
from django.http import HttpResponse

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
    koders = [
        {"name": "Benjamin", "generation": "ig", "bootcamp": "Python"},
        {"name": "Luis", "generation": "ig", "bootcamp": "Python"}
    ]
    return HttpResponse(f"<h1>{koders}<h1>")
