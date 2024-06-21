from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .serializers import VerificarDisponibilidadSerializer, SesionSerializer
from rest_framework.permissions import IsAuthenticated
from core.models import Sesion, Clase
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
def verificar_disponibilidad(request):
    serializer = VerificarDisponibilidadSerializer(data=request.data)
    if serializer.is_valid():
        fecha = serializer.validated_data.get('fecha')
        hora = serializer.validated_data.get('hora')
        clase_id = serializer.validated_data.get('clase_id')
        
        # Verificar si los datos recibidos son los esperados
        print(f"Fecha recibida: {fecha}, Hora recibida: {hora}, Clase ID recibido: {clase_id}")

        try:
            # Intentar combinar fecha y hora en un objeto datetime
            fecha_hora = datetime.strptime(f"{fecha} {hora}", '%d/%m/%Y %H:%M')
            print(f"Fecha y hora combinadas: {fecha_hora}")
        except ValueError as e:
            print(f"Error al convertir fecha y hora: {e}")
            return Response({'error': 'Formato de fecha o hora incorrecto'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si ya existe una sesión con la misma fecha, hora y clase
        sesiones_existentes = Sesion.objects.filter(fechaclase=fecha_hora, clase_id=clase_id)
        print(f"Sesiones encontradas: {sesiones_existentes.count()}")

        if sesiones_existentes.exists():
            return Response({'disponible': False}, status=status.HTTP_200_OK)
        else:
            return Response({'disponible': True}, status=status.HTTP_200_OK)

    # Manejar errores de serializer
    print(f"Errores de serializer: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@permission_classes((IsAuthenticated,))  

@api_view(['POST'])
def crear_sesion(request):
    serializer = SesionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def GenerarToken(request):
    data = JSONParser().parse(request)
    username = data.get('username')
    password = data.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Usuario inválido'}, status=status.HTTP_400_BAD_REQUEST)

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})