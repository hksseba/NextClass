
from django.urls import path
from .views import PaginaPrincipal, Login, Perfil

urlpatterns = [
    
   path('', PaginaPrincipal, name="Paginaprincipal"),
   path('Login', Login, name= "Login"),
   path('Perfil', Perfil, name= "Perfil"),
]
