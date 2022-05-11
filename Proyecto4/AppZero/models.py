from django.db import models

# Create your models here.
class PersLimp(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    DNI = models.IntegerField()
    direccion=models.CharField(max_length=40, blank=True)
    telefono=models.IntegerField(blank=True)
    direccion=models.EmailField(blank=True)

class Autoridad(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    telefono=models.IntegerField()
    cargo=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'El directivo {self.nombre} {self.apellido} con telefono {self.telefono} y cargo {self.cargo}.'

class Alumno(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'El alumno {self.nombre} {self.apellido} con edad {self.edad}.'

class Profesor(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=40)
    DNI = models.IntegerField()
    telefono=models.IntegerField()

    def __str__(self) -> str:
        return f'El profesor {self.nombre} {self.apellido} con telefono {self.telefono} con edad {self.edad} con edad {self.edad} y especialidad {self.especialidad}'
    

class Curso(models.Model):

    materia=models.CharField(max_length=40)
    nivel=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'El curso que contiene la materia {self.materia} correspondiente al nivel {self.nivel}'

class Materia(models.Model):

    nombre=models.CharField(max_length=40)
    nivel=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'La materia {self.nombre} correspondiente al nivel {self.nivel}'