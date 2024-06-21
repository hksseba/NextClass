from rest_framework import serializers
from core.models import Sesion, Clase


class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = ['id_sesion', 'fechaclase', 'contacto', 'mensaje', 'estado_clase', 'profesor', 'estudiante', 'clase']

class VerificarDisponibilidadSerializer(serializers.Serializer):
    fecha = serializers.CharField()
    hora = serializers.CharField()
    clase_id = serializers.IntegerField()

    # api/views.py