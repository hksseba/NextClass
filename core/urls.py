from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

from .views import (PaginaPrincipal, Login, Logueo, Perfil, Solicitudes, PanelAdmin, PerfilProfe, RegistroEstudiante, FormularioEstudiante, 
RegistroProfe, VistaProfe, RegistroAdmin, ListaUsuarios, ListaClases, AceptarSolicitud, RechazarSolicitud, DetalleSolicitud, EliminarUsuario,
EliminarClase, VerClase, Deslogueo, CrearClase, FormClase, ClasesProfe, CambiarContra, reset_password, Agendar, FormularioAgendar, FormularioAdmin,
solicitar_cambio_contra, Calificar, EditarClase , exportar_excel, ValidacionPapas, CorreoPapas, ValidacionPapasView, ModificarPerfil, 
AceptarSolicitudEstudiante,RechazarSolicitudEstudiante,ClasesHistoria, ClasesLenguaje,ClasesMatematica, pagar,retorno,Clases
)

urlpatterns = [    
   path('', PaginaPrincipal, name="PaginaPrincipal"),
   path('Login/', Login, name= "Login"),
   path('Logueo', Logueo, name= "Logueo"),
   path('Solicitudes', Solicitudes, name= "Solicitudes"),
   path('PanelAdmin', PanelAdmin, name= "PanelAdmin"),
   path('PerfilProfe', PerfilProfe, name= "PerfilProfe"),
   path('Perfil', Perfil, name= "Perfil"),
   path('RegistroEstudiante/', RegistroEstudiante, name='RegistroEstudiante'),
   path('FormularioEstudiante/', FormularioEstudiante, name='FormularioEstudiante'),
   path('RegistroProfe/', RegistroProfe, name='RegistroProfe'),
   path('VistaProfe/<int:id_profesor>/<int:id_clase>/',VistaProfe, name='VistaProfe'),
   path('RegistroAdmin/', RegistroAdmin, name='RegistroAdmin'),
   path('ListaUsuarios/', ListaUsuarios, name='ListaUsuarios'),
   path('ListaClases/', ListaClases, name='ListaClases'),
   path('AceptarSolicitud/<int:id_solicitud>/', AceptarSolicitud, name='AceptarSolicitud'),
   path('RechazarSolicitud/<int:id_solicitud>/', RechazarSolicitud, name='RechazarSolicitud'),
   path('solicitudes/detalle/<int:id_solicitud>/', DetalleSolicitud, name='DetalleSolicitud'),
   path('EliminarUsuario/<int:usuario_id>/', EliminarUsuario, name='EliminarUsuario'),
   path('EliminarClase/<int:clase_id>/', views.EliminarClase, name='EliminarClase'),
   path('VerClase/<int:clase_id>/', VerClase, name='VerClase'),
   path('Deslogueo/', Deslogueo, name='Deslogueo'),
   path('CrearClase/', CrearClase, name='CrearClase'),
   path('FormClase/', FormClase, name='FormClase'),
   path('VerClases/', ClasesProfe, name='ClasesProfe'),
   path('CambiarContra/', CambiarContra, name='CambiarContra'),
   path('reset_password/<email>/', views.reset_password, name='reset_password'),
   path('Agendar/<int:id_profesor>/<int:id_clase>/', Agendar, name='Agendar'),
   path('FormularioAdmin/', FormularioAdmin, name='FormularioAdmin'),
   path('solicitar_cambio_contra/<str:tipo>/', views.solicitar_cambio_contra, name='solicitar_cambio_contra'),
   path('Calificar/<int:id_profesor>/<int:id_clase>/', Calificar, name='Calificar'),
   path('EditarClase<id_clase>/', EditarClase, name='EditarClase'),
   path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
   path('validacion_papas/<int:student_id>/<str:decision>/', ValidacionPapas, name='ValidacionPapas'),
   path('CorreoPapas/', CorreoPapas, name='CorreoPapas'),
   path('validacion_papas_view/<int:student_id>/', ValidacionPapasView, name='ValidacionPapasView'),
   path('ModificarPerfil/', ModificarPerfil, name='ModificarPerfil'),
   path('AceptarSolicitudEstudiante/<int:id_estudiante>/', AceptarSolicitudEstudiante, name='AceptarSolicitudEstudiante'),
   path('RechazarSolicitudEstudiante/<int:id_estudiante>/', RechazarSolicitudEstudiante, name='RechazarSolicitudEstudiante'),
   path('ClasesHistoria/', ClasesHistoria, name='ClasesHistoria'),
   path('ClasesLenguaje/', ClasesLenguaje, name='ClasesLenguaje'),
   path('ClasesMatematica', ClasesMatematica, name='ClasesMatematica'),
   path('Clases', Clases, name='Clases'),
   path('pagar/<int:sesion_id>/', pagar, name='pagar'),
   path('retorno/', retorno, name='retorno'),
   path('api/', include('api.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)