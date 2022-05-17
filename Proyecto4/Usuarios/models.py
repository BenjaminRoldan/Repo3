from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20, null=True, choices=[('Docente', 'Docente'), ('Preceptor', 'Preceptor'), ('Recursos Humanos', 'Recursos Humanos'), ('Director', 'Director')])

    def __str__(self):
        return self.user.username