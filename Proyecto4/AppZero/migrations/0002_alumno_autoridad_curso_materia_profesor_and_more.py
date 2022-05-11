# Generated by Django 4.0.2 on 2022-05-03 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Autoridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('cargo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('nivel', models.CharField(max_length=40)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppZero.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Administrativo',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.DeleteModel(
            name='PersonalLimpieza',
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppZero.profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppZero.curso'),
        ),
    ]