from django.db import models

# Create your models here.

# Las clases(modelos) van capitalizadas
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiedad de la clase(modelo) representa un atributo de la tabla

class Koder(models.Model):
    '''Koder Model.'''
    
    
    STATUSES = [
        ("active", "Active"), 
        ("inactive", "Inactive"),
        ("finished", "Finished")
    ]

    SIZES = [
        ("s", "Small"), 
        ("m", "Medium"),
        ("l", "Large")
    ]



    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    generation = models.CharField(max_length=20) # -> string
    email = models.EmailField(unique=True) # -> email único
    phone = models.CharField(max_length=25) # -> núm telefónico
    status = models.CharField(max_length=8, choices= STATUSES, default="active")
    size = models.CharField(max_length=1, choices= SIZES, default="s")
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    # -> En cuanto se cree nos agrega la hora por automático
    updated_at = models.DateTimeField(blank=True, null=True)
    # -> Puede ser nulo a nivel django y nivel base de datos

# Representar como nos regresan el koder
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"


