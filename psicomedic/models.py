from django.db import models
import datetime
import django.utils.timezone

# Create your models here.

class Psychologist(models.Model):
    '''Psychologist Model.'''
    
   
    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    birthdate = models.DateTimeField()
    email = models.EmailField(unique=True) # -> email único
    phone = models.CharField(max_length=25) # -> núm telefónico
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.pk}, Nombre: {self.first_name} {self.last_name}, email: {self.email}, teléfono: {self.phone}"


class Patient(models.Model):
    '''Patient Model.'''


    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    birthdate = models.DateTimeField()
    email = models.EmailField(unique=True) # -> email único
    phone = models.CharField(max_length=25) # -> núm telefónico
    created_at = models.DateTimeField(auto_now_add=True)
    biography = models.CharField(max_length=255)
    address_id = models.CharField(max_length=255)


    def __str__(self):
            return f"id: {self.pk}, Nombre: {self.first_name} {self.last_name}, email: {self.email}, teléfono: {self.phone}"

class Appointment(models.Model):
    '''Appointment Model.'''

    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

# Foreign keys
    psychologist = models.ForeignKey(Psychologist, models.PROTECT, related_name="appointments", blank=True, null=True)
    patient = models.ForeignKey(Patient, models.PROTECT, related_name="appointments", blank=True, null=True)


    def __str__(self):
            return f"Fecha:{self.appointment_date}, creada: {self.created_at}"




