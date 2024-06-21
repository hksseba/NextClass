# api/urls.py
from django.urls import path
from .views import verificar_disponibilidad, crear_sesion, GenerarToken

urlpatterns = [
    path('verificar_disponibilidad/', verificar_disponibilidad, name='verificar_disponibilidad'),
    path('crear_sesion/', crear_sesion, name='crear_sesion'),
    path('GenerarToken/', GenerarToken, name='GenerarToken'),
    
]
