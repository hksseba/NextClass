from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import PaginaPrincipal, Login, EliminarUsuario, VerClase, EliminarClase, Perfil, AceptarSolicitud, RechazarSolicitud, ListaClases, ListaUsuarios, CambiarContra, Solicitudes, PanelAdmin, PerfilProfe, RegistroEstudiante, RegistroProfe , RegistroAdmin , FormularioEstudiante, VistaProfe, Deslogueo, Logueo, CrearClase , FormClase, ClasesProfe, Agendar, reset_password

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
   path('VistaProfe/<int:id_profesor>/', VistaProfe, name='VistaProfe'),
   path('RegistroAdmin/', RegistroAdmin, name='RegistroAdmin'),
   path('ListaUsuarios/', ListaUsuarios, name='ListaUsuarios'),
   path('ListaClases/', ListaClases, name='ListaClases'),
   path('AceptarSolicitud/<int:id_solicitud>/', AceptarSolicitud, name='AceptarSolicitud'),
   path('RechazarSolicitud/<int:id_solicitud>/', RechazarSolicitud, name='RechazarSolicitud'),
   path('EliminarUsuario/<int:usuario_id>/', EliminarUsuario, name='EliminarUsuario'),
   path('EliminarClase/<int:clase_id>/', EliminarClase, name='EliminarClase'),
   path('VerClase/<int:clase_id>/', VerClase, name='VerClase'),
   path('Deslogueo/', Deslogueo, name='Deslogueo'),
   path('CrearClase/', CrearClase, name='CrearClase'),
   path('FormClase/', FormClase, name='FormClase'),
   path('VerClases/', ClasesProfe, name='ClasesProfe'),
   path('Agendar/<int:id_profesor>/', Agendar, name='Agendar'),
   path('CambiarContra/', CambiarContra, name='CambiarContra'),
   path('reset_password/<email>/', views.reset_password, name='reset_password'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

