from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from core.models import Usuario, Estudiante, Profesor, Materia
import re
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    return render(request, 'core/html/PaginaPrincipal.html')

def Login(request):
    return render(request, 'core/Logueo/Login.html')


def Logueo(request):
    if request.method == 'POST':
        correo = request.POST.get('email1')
        contra = request.POST.get('contra1')

        # Buscar al usuario en el modelo personalizado
        try:
            usuario1 = Usuario.objects.get(email=correo)
        except Usuario.DoesNotExist:
            messages.error(request, 'No se encontró el usuario')
            return redirect('Login')

        # Autenticar al usuario utilizando authenticate
        user = authenticate(request, username=usuario1.email, password= usuario1.contra)
        if user is not None:
            login(request, user)
            if usuario1.tipo_de_usuario == "Admin":
                return redirect('PanelAdmin')
            else:
                return redirect('Perfil')
        else:
            messages.error(request, 'La contraseña es incorrecta')
            return redirect('Login')



def CambiarContra (request):
    return render(request, 'core/html/CambiarContra.html')

def Solicitudes (request):
    return render(request, 'core/html/Solicitudes.html')

def PanelAdmin (request):
    return render(request, 'core/html/PanelAdmin.html')

def PerfilProfe (request):
    return render(request, 'core/html/PerfilProfe.html')

def VistaProfe (request):
    return render(request, 'core/html/VistaProfe.html')

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
    
    return render(request, 'core/html/RegistroEstudiante.html')


def FormularioEstudiante(request):
    if request.method == 'POST':
        vFoto = request.FILES.get('fotoAlumno')
        vNombre = request.POST.get('nombre')
        vApellido = request.POST.get('apellido')
        vTelefono = request.POST.get('telefono')
        vCorreo = request.POST.get('email')
        vClave = request.POST.get('contrasena')
        vNvlEducativo = request.POST.get('NvlEducativo')

        # Verificar si el correo electrónico ya está en uso
        if Usuario.objects.filter(email=vCorreo).exists():
            messages.warning(request, 'El correo ya está en uso')
            return redirect('RegistroEstudiante')

        # Crear el usuario personalizado
        usuario = Usuario.objects.create(
            email=vCorreo,
            nombre=vNombre,
            apellido=vApellido,
            telefono=vTelefono,
            contra=vClave,
            foto=vFoto,
            tipo_de_usuario="Estudiante"
        )

        # Crear el usuario de Django asociado
        user = User.objects.create_user(
            username=vCorreo,
            email=vCorreo,
            password=vClave,
            first_name=vNombre,
            last_name=vApellido
        )

        # Crear el estudiante asociado al usuario personalizado
        estudiante = Estudiante.objects.create(
            usuario=usuario,
            nivel_educativo=vNvlEducativo
        )

        messages.success(request, "Registro completado con éxito.")
        return redirect('Login')  # Redirigir después de registrar con éxito



@login_required
def Perfil (request):
    usuario = Usuario.objects.get(email = request.user.username)
    return render(request, 'core/html/Perfil.html', {'usuario': usuario})