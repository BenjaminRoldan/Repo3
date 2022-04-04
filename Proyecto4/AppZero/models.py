from django.db import models

# Create your models here.
class Institucion(models.Model):

    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    nivel=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'La Institución {self.nombre} de nivel {self.nivel} ubicada en {self.direccion}.'

class Administrativo(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()

    def __str__(self) -> str:
        return f'El administrativo {self.nombre} {self.apellido}'

class Docente(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    materia=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'El docente {self.nombre} {self.apellido} de la materia {self.materia}'
    

class PersonalLimpieza(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    turno=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'El personal de limpieza {self.nombre} {self.apellido} del turno {self.turno}'