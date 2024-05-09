from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from core.models import Usuario, Estudiante, Admin, Profesor, Materia, Sesion
import re
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    profesores = Profesor.objects.select_related('usuario').all()
    contexto = {
        "profesores": profesores,
        "user": request.user
    }
    return render(request, 'core/html/PaginaPrincipal.html', contexto)


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

        # Validar la contraseña ingresada con la contraseña almacenada
        if contra == usuario1.contra:
            # Autenticar al usuario utilizando authenticate
            user = authenticate(request, username=usuario1.email, password=usuario1.contra)
            if user is not None:
                login(request, user)
                if usuario1.tipo_de_usuario == "Admin":
                    return redirect('PanelAdmin')
                else:
                    return redirect('Perfil')
            else:
                messages.error(request, 'La contraseña es incorrecta')
                return redirect('Login')
        else:
            messages.error(request, 'La contraseña es incorrecta')
            return redirect('Login')


def Deslogueo(request):
    logout(request)
    return redirect('PaginaPrincipal')

def CambiarContra (request):
    return render(request, 'core/html/CambiarContra.html')

def Solicitudes(request):
    solicitudes = Profesor.objects.filter(estado_de_aprobacion="Pendiente")  # Solo las solicitudes pendientes
    return render(request, 'core/html/Solicitudes.html', {'solicitudes': solicitudes})

# Vista para aceptar una solicitud
def AceptarSolicitud(request, id_solicitud):
    try:
        profesor = Profesor.objects.get(id_profesor=id_solicitud)
        profesor.estado_de_aprobacion = "Aprobado"  # Cambiar el estado a Aprobado
        profesor.save()  # Guardar los cambios
        messages.success(request, "Solicitud aceptada con éxito.")
    except Profesor.DoesNotExist:
        messages.error(request, "Solicitud no encontrada.")
    return redirect('Solicitudes')  # Redirigir a la página de solicitudes

# Vista para rechazar una solicitud
def RechazarSolicitud(request, id_solicitud):
    try:
        profesor = Profesor.objects.get(id_profesor=id_solicitud)
        
        # Al rechazar, eliminamos el profesor
        usuario = profesor.usuario  # Obtiene el usuario asociado
        profesor.delete()  # Elimina el registro del profesor

        # Ahora, eliminamos el usuario asociado
        usuario.delete()  # Elimina el registro del usuario
        
        messages.success(request, "Solicitud rechazada y usuario eliminado con éxito.")
    except Profesor.DoesNotExist:
        messages.error(request, "Solicitud no encontrada.")
    except Usuario.DoesNotExist:
        messages.error(request, "Usuario no encontrado.")  # En caso de error al eliminar el usuario

    return redirect('Solicitudes')  # Redirigir a la página de solicitudes

def PanelAdmin(request):

    total_usuarios = Usuario.objects.count()
    total_profesores = Profesor.objects.count()
    total_solicitudes = Profesor.objects.filter(estado_de_aprobacion='Pendiente').count()

    context = {
        'total_usuarios': total_usuarios,
        'total_profesores': total_profesores,
        'total_solicitudes': total_solicitudes,
    }

    return render(request, 'core/html/PanelAdmin.html', context)

def PerfilProfe (request):
    return render(request, 'core/html/PerfilProfe.html')


def VistaProfe (request, id):
    profe = Profesor.objects.select_related('usuario').get(id_profesor=id)
    contexto = {
        "p": profe
    }
    return render(request, 'core/html/VistaProfe.html', contexto)

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

        # Verificar si el correo electrónico ya está en uso
        if Usuario.objects.filter(email=email).exists():
            messages.warning(request, 'El correo ya está en uso')
            return redirect('RegistroProfe')

        # Crear el usuario personalizado
        usuario = Usuario.objects.create(
            email=email,
            nombre=nombre,
            run=run,
            edad=edad,
            apellido=apellido,
            telefono=telefono,
            contra=contra,
            foto=foto,
            tipo_de_usuario="Profesor"
        )

        # Crear el usuario de Django asociado
        user = User.objects.create_user(
            username=email,
            email=email,
            password=contra,
            first_name=nombre,
            last_name=apellido
        )

        # Crear el estudiante asociado al usuario personalizado
        profesor = Profesor.objects.create(
            usuario=usuario,
            antecedentes=antecedentes,
            tarifa=tarifa,
            especializacion=especializacion,
            descripcion=descripcion,
             estado_de_aprobacion="Pendiente"
        )

        messages.success(request, "Registro completado con éxito.")
        return redirect('Login')  # Redirigir después de registrar con éxito


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

def RegistroAdmin(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contra = request.POST.get('contra')
        telefono = request.POST.get('telefono', '')
        foto = request.FILES.get('foto', None)  # Si hay una imagen, se procesa
        run = request.POST.get('run')

        # Validaciones
        if not nombre or not apellido or not email or not contra or not run:
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'core/html/RegistroAdmin.html')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Correo electrónico no es válido.")
            return render(request, 'core/html/RegistroAdmin.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Ya existe un usuario con este correo.")
            return render(request, 'core/html/RegistroAdmin.html')

        try:
            # Crear usuario personalizado
            usuario = Usuario(
                email=email,
                nombre=nombre,
                apellido=apellido,
                contra=contra,
                tipo_de_usuario='Admin',
                telefono=telefono,
                foto=foto,
                run=run
            )
            usuario.save()

            # Crear usuario Django para autenticación
            user = User.objects.create_user(
                username=email,
                email=email,
                password=contra,
                first_name=nombre,
                last_name=apellido
            )

            # Crear el perfil de Admin
            admin = Admin(
                usuario=usuario,
                nombre=nombre,
            )
            admin.save()

            messages.success(request, "Administrador creado con éxito.")
            return redirect('PanelAdmin')  # Redirigir al panel del administrador

        except Exception as e:
            messages.error(request, f"Error al crear el administrador: {e}")

    return render(request, 'core/html/RegistroAdmin.html')

@login_required
def Perfil (request):
    usuario = Usuario.objects.get(email = request.user.username)
    return render(request, 'core/html/Perfil.html', {'usuario': usuario})

def ListaUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'core/html/ListaUsuarios.html', {'usuarios': usuarios})

def ListaClases(request):
    clases = Sesion.objects.all()
    return render(request, 'core/html/ListaClases.html', {'clases': clases})

def EliminarUsuario(request, usuario_id):
    try:
        # Buscar el usuario por ID
        usuario = Usuario.objects.get(id_usuario=usuario_id)

        # Eliminar el usuario
        usuario.delete()

        # Mensaje de éxito
        messages.success(request, f"Usuario {usuario.nombre} {usuario.apellido} eliminado con éxito.")

    except Usuario.DoesNotExist:
        # Manejar caso donde el usuario no exista
        messages.error(request, "Usuario no encontrado.")

    except Exception as e:
        # Manejar otros errores inesperados
        messages.error(request, f"Error al eliminar usuario: {e}")

    # Redirigir a la lista de usuarios
    return redirect('ListaUsuarios')

def EliminarClase(request, clase_id):
    try:
        # Obtén la clase y elimínala
        clase = Sesion.objects.get(id_sesion=clase_id)
        clase.delete()
        messages.success(request, f"Clase eliminada con éxito.")
    except Sesion.DoesNotExist:
        messages.error(request, "Clase no encontrada.")
    except Exception as e:
        messages.error(request, f"Error al eliminar clase: {e}")

    # Redirigir a una página después de la eliminación, como la lista de clases
    return redirect('ListaClases')

def VerClase(request, clase_id):
    # Obtén la clase correspondiente al ID o devuelve un 404 si no existe
    clase = get_object_or_404(Sesion, id_sesion=clase_id)
    return render(request, 'core/html/VerClase.html', {'clase': clase})