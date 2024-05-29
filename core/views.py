from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime

from django.contrib.auth import authenticate, login

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count, Avg
from core.models import Usuario, Estudiante, Admin, Profesor, Clase, Materia, Sesion, Evaluacion
import re
# Create your views here.


from django.shortcuts import render

def PaginaPrincipal(request):
    profesores = Profesor.objects.select_related('usuario').all()
    clase = Clase.objects.select_related('pro')
    materias = Materia.objects.all()
    print( materias)
    contexto = {
        "profesores": profesores,
        "user": request.user,
        "materias":materias,
        "clase": clase
    }
    return render(request, 'core/html/PaginaPrincipal.html', contexto)


def Login(request):
    return render(request, 'core/Logueo/Login.html')

from django.contrib import messages

from django.contrib import messages

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
                
                # Verificar el tipo de usuario
                if usuario1.tipo_de_usuario == "Admin":
                    return redirect('PanelAdmin')
                elif usuario1.tipo_de_usuario == "Estudiante":
                    return redirect('Perfil')
                elif usuario1.tipo_de_usuario == "Profesor": 
                    # Verificar el estado de aprobación del profesor
                    try:
                        profesor = Profesor.objects.get(usuario=usuario1)
                        if profesor.estado_de_aprobacion == 'Pendiente':
                            messages.error(request, 'Tu cuenta está pendiente de aprobación. Por favor, espera la aprobación para iniciar sesión.')
                            return redirect('Login')
                        else:
                            return redirect('Perfil')
                    except Profesor.DoesNotExist:
                        messages.error(request, 'Tu cuenta de profesor no está configurada correctamente.')
                        return redirect('Login')
            else:
                messages.error(request, 'La contraseña es incorrecta')
                return redirect('Login')
        else:
            messages.error(request, 'La contraseña es incorrecta')
            return redirect('Login')

def Deslogueo(request):
    logout(request)
    return redirect('PaginaPrincipal')

def Agendar (request, id_profesor):
    profe = Profesor.objects.select_related('usuario').get(id_profesor=id_profesor)
    usuario = Usuario.objects.get(email = request.user.username)
    clase = Clase.objects.get(profesor = profe)
    contexto = {
        "profe": profe,
        "clase": clase,
        "usuario": usuario
    }
    return render(request, 'core/html/Agendar.html', contexto)
    
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
    # Total de usuarios
    total_usuarios = Usuario.objects.count()
    total_profesores = Profesor.objects.count()
    total_solicitudes = Profesor.objects.filter(estado_de_aprobacion='Pendiente').count()

    # Distribución de usuarios por rol
    usuarios_por_rol = Usuario.objects.values('tipo_de_usuario').annotate(count=Count('tipo_de_usuario'))

    # Número total de clases
    total_clases = Clase.objects.count()

    # Clases por categoría/tema
    clases_por_categoria = Clase.objects.values('descripcion_clase').annotate(count=Count('descripcion_clase'))

    # Número de clases por profesor
    clases_por_profesor = Clase.objects.values('profesor__usuario__nombre').annotate(count=Count('id_clase'))

    # Tasa de ocupación de las clases
    ocupacion_promedio = Sesion.objects.aggregate(avg_ocupacion=Avg('id_sesion'))

    # Evaluaciones promedio de las clases
    evaluacion_promedio = Evaluacion.objects.aggregate(avg_evaluacion=Avg('valoracion'))

    # Preferencias de los estudiantes por rangos de edad
    preferencias_edad = Sesion.objects.values('estudiante__usuario__edad').annotate(
        avg_prof_edad=Avg('profesor__usuario__edad'),
        count_prof_genero=Count('profesor__usuario__tipo_de_usuario'),
        count_clases=Count('id_sesion')
    ).order_by('estudiante__usuario__edad')

    context = {
        'total_usuarios': total_usuarios,
        'total_profesores': total_profesores,
        'total_solicitudes': total_solicitudes,
        'usuarios_por_rol': usuarios_por_rol,
        'total_clases': total_clases,
        'clases_por_categoria': clases_por_categoria,
        'clases_por_profesor': clases_por_profesor,
        'ocupacion_promedio': ocupacion_promedio,
        'evaluacion_promedio': evaluacion_promedio,
        'preferencias_edad': preferencias_edad,
    }

    return render(request, 'core/html/PanelAdmin.html', context)


def PerfilProfe (request):
    return render(request, 'core/html/PerfilProfe.html')


def VistaProfe (request, id_profesor, id_clase):
    profe = Profesor.objects.select_related('usuario').get(id_profesor=id_profesor)
    clase = Clase.objects.select_related('profesor').get(id_clase=id_clase)

    contexto = {
        "profe": profe,
        "clase": clase
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
        descripcion = request.POST.get('descripcion')
        run = request.POST.get('run')
        foto = request.FILES.get('foto_profe')
        carnet = request.FILES.get('carnet')
        antecedentes = request.FILES.get('antecedentes')
        contra = request.POST.get('contra')

        # Verificar si el correo electrónico ya está en uso
        if Usuario.objects.filter(email=email).exists():
            messages.warning(request, 'El correo ya está en uso')
            return redirect('RegistroProfe')

        # Crear el usuario personalizado
        usuario = Usuario.objects.create(
            email=email,
            nombre=nombre,
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
            run=run,
            carnet=carnet,
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

        # Validaciones
        if not nombre or not apellido or not email or not contra:
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

def CambiarContra(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            send_email(email, request)
            return HttpResponse("Solicitud de cambio de contraseña enviada.")  # Respuesta después de procesar el POST
        except User.DoesNotExist:
            messages.error(request, 'El correo electrónico no está registrado.')
    
    return render(request, 'core/html/CambiarContra.html')

def send_email(email, request):
    user = User.objects.get(email=email)
    context = {
        'email': email,
        'request': request,
    }

    template = get_template('core/html/correo.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Cambio de Contraseña',
        'Código de Restablecimiento',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()

def reset_password(request, email):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            usuario = get_object_or_404(Usuario, email=email)
            
            # Actualizar la contraseña en el modelo User de Django
            user.set_password(new_password)
            user.save()

            # Actualizar la contraseña en el modelo Usuario personalizado
            usuario.contra = new_password
            usuario.save()

            # Mantener al usuario autenticado después de cambiar la contraseña
            update_session_auth_hash(request, user)
            
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('Login')  # Redirigir al perfil del usuario
        except User.DoesNotExist:
            messages.error(request, 'El correo electrónico no está registrado.')
    return render(request, 'core/html/reset_password.html', {'email': email})

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

def FormClase(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        usuario = request.user
        usuario1 = Usuario.objects.get(email = usuario)
        idusuario = Profesor.objects.get(usuario = usuario1)
        try:
            # Crear usuario personalizado
            clase = Clase(
                nombre_clase=titulo,
                tarifa_clase = precio,
                descripcion_clase=descripcion,
                profesor = idusuario                
            )
            clase.save()
            return redirect('Perfil')
            
        except Exception as e:
            messages.error(request, f"Error al crear la clase: {e}")
            return redirect('CrearClase')

def CrearClase(request):
    clases = Clase.objects.all()
    return render(request, 'core/html/FormClase.html', {'clases': clases })            

def ClasesProfe(request):
    usuario = request.user
    usuario1 = Usuario.objects.get(email = usuario)
    profe = Profesor.objects.get(usuario = usuario1)
    clases = Clase.objects.get(profesor = profe)

    return render (request, 'core/html/VerClases.html', {'clases' : clases} )

def Agendar (request, id_profesor, id_clase):
    profe = Profesor.objects.select_related('usuario').get(id_profesor=id_profesor)
    usuario = Usuario.objects.get(email = request.user.username)
    clase = Clase.objects.select_related('profesor').get(id_clase=id_clase)
    contexto = {
        "profe": profe,
        "clase": clase,
        "usuario": usuario
    }
    return render(request, 'core/html/Agendar.html', contexto)

def FormularioAgendar(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        fecha_str = request.POST.get('datepicker')
        telefono = request.POST.get('telefono')
        id_profesor = request.POST.get('id_profesor')
        usuario_actual = request.user
        usuario = get_object_or_404(Usuario, email=usuario_actual.email)
        estudiante = get_object_or_404(Estudiante, usuario=usuario)
        id_estudiante = estudiante.id_estudiante

        fecha = datetime.strptime(fecha_str, '%d/%m/%Y').strftime('%Y-%m-%d')

                
        nueva_sesion = Sesion.objects.create(
            mensaje=mensaje,
            fechaclase=fecha,
            contacto=telefono,
            profesor_id=id_profesor,
            estudiante_id=id_estudiante
        )
        print("ID del estudiante:", id_estudiante)
        
    
    return render(request, 'core/html/Agendar.html')

def Calificar(request):
    if request.method == 'POST':
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        usuario = get_object_or_404(Usuario, email=usuario_actual.email)

        # Guarda la calificación en la base de datos (aquí debes ajustar el código según tu modelo de Django)
        calificar = Evaluacion.objects.create(
            recomendacion=comentario,
            valoracion=calificacion,
            profesor_id=id_profesor,
            estudiante_id=id_estudiante
        )
        nueva_evaluacion = Evaluacion(valoracion=calificacion)
        nueva_evaluacion.save()
        return HttpResponse('Calificación guardada exitosamente')
    else:
        return HttpResponse('Método no permitido')
    comentario = request.POST.get('comentario')
    calificacion = request.POST.get('')














    # def SolicitudesClase(request):
    #     solicitudes = Profesor.objects.filter(estado_clase="Pendiente")  # Solo las solicitudes pendientes
    # return render(request, 'core/html/VerClases.html', {'solicitudes': solicitudes})

    # def AceptarClase(request, id_solicitud):
    # try:
    #     profesor = Profesor.objects.get(id_profesor=id_solicitud)
    #     profesor.estado_de_aprobacion = "Aprobado"  # Cambiar el estado a Aprobado
    #     profesor.save()  # Guardar los cambios
    #     messages.success(request, "Solicitud aceptada con éxito.")
    # except Profesor.DoesNotExist:
    #     messages.error(request, "Solicitud no encontrada.")
    # return redirect('Solicitudes')  # Redirigir a la página de solicitudes
