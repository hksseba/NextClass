
from django.urls import path
from .views import PaginaPrincipal, Login

urlpatterns = [
    
   path('', PaginaPrincipal, name="Paginaprincipal"),
   path('Login', Login, name= "Login")
]
