from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PaginaPrincipal, Login, Perfil, AceptarSolicitud, RechazarSolicitud, ListaClases, ListaUsuarios, CambiarContra, Solicitudes, PanelAdmin, PerfilProfe, RegistroEstudiante, RegistroProfe , RegistroAdmin , FormularioEstudiante, Logueo
from .views import PaginaPrincipal, Login, Perfil, AceptarSolicitud, RechazarSolicitud, ListaClases, ListaUsuarios, CambiarContra, Solicitudes, PanelAdmin, PerfilProfe, RegistroEstudiante, RegistroProfe , RegistroAdmin , FormularioEstudiante, VistaProfe, Deslogueo

urlpatterns = [    
   path('', PaginaPrincipal, name="PaginaPrincipal"),
   path('Login/', Login, name= "Login"),
   path('Logueo', Logueo, name= "Logueo"),
   path('Perfil', Perfil, name= "Perfil"),
   path('CambiarContra', CambiarContra, name= "CambiarContra"),
   path('Solicitudes', Solicitudes, name= "Solicitudes"),
   path('PanelAdmin', PanelAdmin, name= "PanelAdmin"),
   path('PerfilProfe', PerfilProfe, name= "PerfilProfe"),
   path('RegistroEstudiante/', RegistroEstudiante, name='RegistroEstudiante'),
   path('FormularioEstudiante/', FormularioEstudiante, name='FormularioEstudiante'),
   path('RegistroProfe/', RegistroProfe, name='RegistroProfe'),
   path('VistaProfe/', VistaProfe, name='VistaProfe'),
   path('RegistroAdmin/', RegistroAdmin, name='RegistroAdmin'),
   path('ListaUsuarios/', ListaUsuarios, name='ListaUsuarios'),
   path('ListaClases/', ListaClases, name='ListaClases'),
   path('AceptarSolicitud/<int:id_solicitud>/', AceptarSolicitud, name='AceptarSolicitud'),
    path('RechazarSolicitud/<int:id_solicitud>/', RechazarSolicitud, name='RechazarSolicitud'),
   path('Deslogueo/', Deslogueo, name='Deslogueo'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

