from django.urls import path

from . import views

urlpatterns = [
    path('led/turnOn/', views.turnOn, name='led-turnOn'),
    path('led/turnOff/', views.turnOff, name='led-turnOff'),
]
