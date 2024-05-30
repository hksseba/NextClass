from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


from .views import PaginaPrincipal, Login, EliminarUsuario, VerClase, EliminarClase, Perfil, AceptarSolicitud, RechazarSolicitud, ListaClases, ListaUsuarios, CambiarContra, Solicitudes, PanelAdmin, PerfilProfe, RegistroEstudiante, RegistroProfe , RegistroAdmin , FormularioEstudiante, VistaProfe, Deslogueo, Logueo, CrearClase , FormClase, ClasesProfe, Agendar, FormularioAgendar, reset_password, Calificar, solicitar_cambio_contra, DetalleSolicitud

urlpatterns = [    
   path('', PaginaPrincipal, name="PaginaPrincipal"),
   path('Login/', Login, name= "Login"),
   path('Logueo', Logueo, name= "Logueo"),
   path('Perfil', Perfil, name= "Perfil"),
   path('Solicitudes', Solicitudes, name= "Solicitudes"),
   path('PanelAdmin', PanelAdmin, name= "PanelAdmin"),
   path('PerfilProfe', PerfilProfe, name= "PerfilProfe"),
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
   path('EliminarClase/<int:clase_id>/', EliminarClase, name='EliminarClase'),
   path('VerClase/<int:clase_id>/', VerClase, name='VerClase'),
   path('Deslogueo/', Deslogueo, name='Deslogueo'),
   path('CrearClase/', CrearClase, name='CrearClase'),
   path('FormClase/', FormClase, name='FormClase'),
   path('VerClases/', ClasesProfe, name='ClasesProfe'),
   path('CambiarContra/', CambiarContra, name='CambiarContra'),
   path('reset_password/<email>/', views.reset_password, name='reset_password'),
   path('Agendar/<int:id_profesor>/<int:id_clase>/', Agendar, name='Agendar'),
   path('FormularioAgendar/', FormularioAgendar, name='FormularioAgendar'),
   path('solicitar_cambio_contra/<str:tipo>/', views.solicitar_cambio_contra, name='solicitar_cambio_contra'),
   path('Calificar/<int:id_profesor>/<int:id_clase>/', Calificar, name='Calificar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

