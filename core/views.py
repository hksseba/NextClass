from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from core.models import Usuario, Estudiante, Profesor, Materia
import re
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    return render(request, 'core/html/PaginaPrincipal.html')

def Login(request):
    return render(request, 'core/Logueo/Login.html')

def CambiarContra (request):
    return render(request, 'core/html/CambiarContra.html')

def Solicitudes (request):
    return render(request, 'core/html/Solicitudes.html')

def PanelAdmin (request):
    return render(request, 'core/html/PanelAdmin.html')

def PerfilProfe (request):
    return render(request, 'core/html/PerfilProfe.html')

def RegistroProfe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        telefono = request.POST.get('telefono')
        especializacion = request.POST.get('especializacion')
        tarifa = request.POST.get('tarifa')
        descripcion = request.POST.get('descripcion')
        run = request.POST.get('run')
        foto = request.POST.get('foto_profe')
        antecedentes = request.POST.get('antecedentes')
        contra = request.POST.get('contra')

        # Validaciones
        if not email or not nombre or not apellido or not especializacion or not tarifa:
            messages.error(request, "Los campos obligatorios deben ser completados.")
            return render(request, 'core/html/RegistroProfe.html', context={"materias": Materia.objects.all()})

        # Validar formato del email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Formato de correo electrónico no válido.")
            return render(request, 'core/html/RegistroProfe.html', context={"materias": Materia.objects.all()})
            
        # Validar formato del run
        if not re.match(r"^[0-9]+-[0-9kK]{1}$", run):
            messages.error(request, "El run debe tener el formato '12345678-9'.")
            return render(request, 'core/html/RegistroEstudiante.html', context={"materias": Materia.objects.all()})

        try:
            usuario = Usuario(
                email=email,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                edad=edad,
                run=run,
                tipo_de_usuario="Profesor",
                foto=foto,
                contra=contra,
            )
            usuario.save()

            profesor = Profesor(
                usuario=usuario,
                especializacion=especializacion,
                tarifa=tarifa,
                antecedentes=antecedentes,
                estado_de_aprobacion="Pendiente",
                descripcion=descripcion,
            )
            profesor.save()

            messages.success(request, "Registro completado con éxito.")
            return redirect('Login')

        except Exception as e:
            messages.error(request, f"Error al registrar: {e}")

    return render(request, 'core/html/RegistroProfe.html', context={"materias": Materia.objects.all()})

def RegistroEstudiante(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        run = request.POST.get('run')
        nivel_educativo = request.POST.get('nivel_educativo')
        descripcion = request.POST.get('descripcion')

        # Validaciones
        if not email or not nombre or not apellido or not nivel_educativo:
            messages.error(request, "Los campos obligatorios deben ser completados.")
            return render(request, 'core/html/RegistroEstudiante.html')

        # Validar formato del email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Formato de correo electrónico no válido.")
            return render(request, 'core/html/RegistroEstudiante.html')

        # Validar formato del run
        if not re.match(r"^[0-9]+-[0-9kK]{1}$", run):
            messages.error(request, "El run debe tener el formato '12345678-9'.")
            return render(request, 'core/html/RegistroEstudiante.html')

        # Crear el usuario y el estudiante
        try:
            usuario = Usuario(
                email=email,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                run=run,
                tipo_de_usuario="Estudiante",
            )
            usuario.save()

            estudiante = Estudiante(
                usuario=usuario,
                nivel_educativo=nivel_educativo,
                descripcion=descripcion,
            )
            estudiante.save()

            messages.success(request, "Registro completado con éxito.")
            return redirect('PaginaPrincipal')  # Redirigir después de registrar con éxito

        except Exception as e:
            messages.error(request, f"Error al registrar: {e}")

    # Mostrar la página para el método GET
    return render(request, 'core/html/RegistroEstudiante.html')

@login_required
def Perfil (request):
    return render(request, 'core/html/Perfil.html')