from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user} - {self.cargo}'