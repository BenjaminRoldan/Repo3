# Generated by Django 4.0.2 on 2022-05-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_userprofile_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cargo',
            field=models.CharField(choices=[('Docente', 'Docente'), ('Preceptor', 'Preceptor'), ('Recursos Humanos', 'Recursos Humanos'), ('Director', 'Director')], max_length=20, null=True),
        ),
    ]
