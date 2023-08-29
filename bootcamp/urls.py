from django.contrib import admin
from django.urls import path

# Views
from .views import get_koder, list_koders

urlpatterns = [
    # Custom URLs
    path("koders/", list_koders),
    path("koders/<int:id>", get_koder)
]