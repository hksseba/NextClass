from django.db import models

# Create your models here.
# Tabla Usuario
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='media', null=True, blank=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.CharField(max_length=3)
    email = models.EmailField(unique=True)
    contra = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True)    
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
    run = models.CharField(max_length=10)
    antecedentes = models.FileField(upload_to='archivos_pdf', null=False)
    carnet = models.ImageField(upload_to='media', null=False)
    especializacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado_de_aprobacion = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre_clase = models.CharField(max_length=255)
    tarifa_clase = models.IntegerField()
    idioma_clase = models.CharField(max_length=255)
    descripcion_clase = models.CharField(max_length=255)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)


# Tabla Materia
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    creado_por = models.ForeignKey(Admin, on_delete=models.CASCADE)

# Tabla Sesion
class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    fechaclase = models.DateField()
    contacto = models.CharField(max_length=15, blank=True)
    mensaje = models.TextField(default="")
    estado_clase = models.CharField(max_length=50, default="Pendiente")
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
 

# Tabla Evaluacion
class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    recomendacion = models.CharField(max_length=700, blank=True, null=True)
    valoracion = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)