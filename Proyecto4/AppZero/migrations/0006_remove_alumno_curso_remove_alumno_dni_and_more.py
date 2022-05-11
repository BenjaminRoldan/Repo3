# Generated by Django 4.0.2 on 2022-05-05 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0005_calificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='autoridad',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='dni',
        ),
        migrations.AddField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='materia',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(max_length=40),
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='especialidad',
        ),
        migrations.AddField(
            model_name='profesor',
            name='especialidad',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Calificacion',
        ),
    ]