from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    return render(request, 'core/html/PaginaPrincipal.html')

def Login (request):
    return render(request, 'core/Logueo/Login.html')
