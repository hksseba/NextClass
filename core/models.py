from django.db import models

# Create your models here.
# Tabla Usuario
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    run = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True)
    foto = models.CharField(max_length=255)
    carnet = models.CharField(max_length=255)
    tipo_de_usuario = models.CharField(max_length=20)

# Tabla Estudiante
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nivel_educativo = models.CharField(max_length=255)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Tabla Admin
class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Tabla Profesor
class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    antecedentes = models.CharField(max_length=255)
    especializacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado_de_aprobacion = models.CharField(max_length=50)
    tarifa = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Tabla Materia
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(Admin, on_delete=models.CASCADE)

# Tabla Sesion
class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    fechadeinicio = models.DateField()
    fechadetermino = models.DateField()
    horadeinicio = models.TimeField()
    horadetermino = models.TimeField()
    enlacedesesion = models.URLField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

# Tabla Evaluacion
class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    recomendacion = models.CharField(max_length=255, blank=True, null=True)
    valoracion = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)