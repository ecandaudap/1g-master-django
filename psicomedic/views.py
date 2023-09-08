from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

from psicomedic.models import Appointment, Psychologist, Patient
import datetime

def list_psychologists(request):
    psychologists = Psychologist.objects.all()
    context = {"psychologists": psychologists}
    template = loader.get_template("psicomedic/list_psychologists.html")

    return HttpResponse(template.render(context, request))

def list_patients(request):
    patients = Patient.objects.all()
    context = {"patients": patients}
    template = loader.get_template("psicomedic/list_patients.html")

    return HttpResponse(template.render(context, request))

def list_appointments(request):
    appointments = Appointment.objects.all()
    context = {"appointments": appointments}
    template = loader.get_template("psicomedic/list_appointments.html")

    return HttpResponse(template.render(context, request))

def get_psychologist(request, id):
    psychologists = Psychologist.objects.get(pk=id)

    return HttpResponse(f"Datos del Psicologo encontrado --->>> {psychologists}")

def get_patient(request, id):
    patients = Patient.objects.get(pk=id)

    return HttpResponse(f"Datos del Paciente --->>> {patients}")

def get_appointment(request, id):
    appointments = Appointment.objects.get(pk=id)

    return HttpResponse(f"Cita encontrada --->>> {appointments}")