# Generated by Django 4.0.2 on 2022-05-05 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0006_remove_alumno_curso_remove_alumno_dni_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='edad',
            new_name='DNI',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='edad',
        ),
    ]
