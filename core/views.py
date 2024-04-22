from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    return render(request, 'core/html/PaginaPrincipal.html')

def Login (request):
    return render(request, 'core/Logueo/Login.html')

def Perfil (request):
    return render(request, 'core/html/Perfil.html')

def CambiarContra (request):
    return render(request, 'core/html/CambiarContra.html')

def Solicitudes (request):
    return render(request, 'core/html/Solicitudes.html')

def PanelAdmin (request):
    return render(request, 'core/html/PanelAdmin.html')

def PerfilProfe (request):
    return render(request, 'core/html/PerfilProfe.html')