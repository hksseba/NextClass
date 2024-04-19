
from django.urls import path
from .views import PaginaPrincipal

urlpatterns = [
    
   path('', PaginaPrincipal, name="paginaprincipal"),
]
