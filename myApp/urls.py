from django.contrib import admin
from django.urls import path

# Views
from .views import bienvenida, despedida, saludo, saludar_con_nombre, saludar_tipo, saludar_con_nombre2

urlpatterns = [
    # Custom URLs
    path("", bienvenida),
    path("despedida/", despedida),
    path("saludo/", saludo),
    path("saludo/<str:nombre>", saludar_con_nombre),
    path("kodemia/<str:type>", saludar_tipo),
    path("saludo/<str:nombre>/<str:type>", saludar_con_nombre2)
]