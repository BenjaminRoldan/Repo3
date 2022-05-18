from django.db import models

# Create your models here.
class PersLimp(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    DNI = models.IntegerField()
    direccion=models.CharField(max_length=60, blank=True, null=True)
    telefono=models.IntegerField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    turno = models.CharField(max_length=40)

    def __str__(self):
        return f'Personal de limpieza {self.nombre} {self.apellido}'

class Autoridad(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    DNI = models.IntegerField()
    direccion=models.CharField(max_length=60, blank=True, null=True)
    telefono=models.IntegerField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    cargo = models.CharField(max_length=40)

    def __str__(self):
        return f'Autoridad {self.nombre} {self.apellido} - {self.cargo}'

class Docente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    DNI = models.IntegerField()
    direccion=models.CharField(max_length=60, blank=True, null=True)
    telefono=models.IntegerField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    profesorado = models.CharField(max_length=40)

    def __str__(self):
        return f'Docente {self.nombre} {self.apellido}'

class Grado(models.Model):
    grado=models.CharField(max_length=1)

    def __str__(self):
        return f'{self.grado}° Grado'

class Curso(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, null=True)
    division=models.CharField(max_length=1)

    def __str__(self):
        return f'Curso {self.division} del {self.grado}'

class Materia(models.Model):
    nombre=models.CharField(max_length=40)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Materia {self.nombre}'

class Alumno(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    DNI = models.IntegerField()
    direccion=models.CharField(max_length=60, blank=True, null=True)
    telefono=models.IntegerField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    calificaciones = models.OneToOneField('Calificacion', null=True, on_delete=models.CASCADE, related_name='+' )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'Alumno/a {self.nombre} {self.apellido}'

class Nota(models.Model):
    C1 = models.FloatField(null=True, blank=True)
    C2 = models.FloatField(null=True, blank=True)
    C3 = models.FloatField(null=True, blank=True)
    

class Calificacion(models.Model):
    matematicas = models.OneToOneField(Nota, on_delete=models.CASCADE, related_name='+', null=True)
    cienciasnaturales = models.OneToOneField(Nota, on_delete=models.CASCADE, related_name='+', null=True)
    cienciassociales = models.OneToOneField(Nota, on_delete=models.CASCADE, related_name='+', null=True)
    ingles = models.OneToOneField(Nota, on_delete=models.CASCADE, related_name='+', null=True)
    educacionfisica = models.OneToOneField(Nota, on_delete=models.CASCADE, related_name='+', null=True)




