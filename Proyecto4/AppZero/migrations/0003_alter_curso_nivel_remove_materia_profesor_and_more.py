# Generated by Django 4.0.2 on 2022-05-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0002_alumno_autoridad_curso_materia_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='materia',
            name='profesor',
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ManyToManyField(to='AppZero.Profesor'),
        ),
    ]