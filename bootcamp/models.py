from django.db import models

# Create your models here.

# Las clases(modelos) van capitalizadas
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiedad de la clase(modelo) representa un atributo de la tabla

# La foreign Key se pone en la N en las relaciones 1 - N
# Cuando hay N - N la FK se pone en la de menors jerarquía
# 1 generation - N koders
# N mentors - N generations
#1 bootcamp - N generations

class Bootcamp(models.Model):
    '''Bootcamp Model.'''

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.name}"

class Generation(models.Model):
    '''Generation Model.'''

    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Foreign keys
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")


    def __str__(self):
        return f"{self.number} python manage{self.bootcamp.name}"

class Koder(models.Model):
    '''Koder Model.'''
    
    
    STATUSES = [
        ("active", "Active"), 
        ("inactive", "Inactive"),
        ("finished", "Finished")
    ]

   
    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    email = models.EmailField(unique=True) # -> email único
    phone = models.CharField(max_length=25) # -> núm telefónico
    status = models.CharField(max_length=8, choices= STATUSES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    # -> En cuanto se crea nos agrega la hora por automático

# Foreign keys
    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")

# Representar como nos regresan el koder
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"


class Mentor(models.Model):
    '''Mentor Model.'''


    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    email = models.EmailField(unique=True) # -> email único
    phone = models.CharField(max_length=25) # -> núm telefónico
    created_at = models.DateTimeField(auto_now_add=True)

# Foreign keys
    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
            return f"id: {self.pk} {self.first_name} {self.last_name}"




