
from django.urls import path
from .views import PaginaPrincipal, Login, Perfil, CambiarContra, Solicitudes, PanelAdmin, PerfilProfe

urlpatterns = [
    
   path('', PaginaPrincipal, name="Paginaprincipal"),
   path('Login', Login, name= "Login"),
   path('Perfil', Perfil, name= "Perfil"),
   path('CambiarContra', CambiarContra, name= "CambiarContra"),
   path('Solicitudes', Solicitudes, name= "Solicitudes"),
   path('PanelAdmin', PanelAdmin, name= "PanelAdmin"),
   path('PerfilProfe', PerfilProfe, name= "PerfilProfe"),
]
