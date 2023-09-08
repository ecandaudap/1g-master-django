#from django.contrib import admin
from django.urls import path

# Views
from .views import list_psychologists, list_patients, list_appointments, get_psychologist, get_patient, get_appointment

urlpatterns = [
    # Custom URLs
    path("psychologists/", list_psychologists),
    path("patients/", list_patients),
    path("appointments/", list_appointments),
    path("psychologists/<int:id>", get_psychologist),
    path("patients/<int:id>", get_patient),
    path("appointments/<int:id>", get_appointment),
    #path("mentors/", list_mentors)
]