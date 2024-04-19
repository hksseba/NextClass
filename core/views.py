from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    # Renderiza la plantilla sin pasar ningún contexto
    return render(request, 'core/html/PaginaPrincipal.html')
