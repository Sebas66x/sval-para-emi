from django.urls import path
from . import views

urlpatterns = [
    path("", views.acceso, name="acceso"),
    path("inicio/", views.sorpresa, name="sorpresa"),
]
