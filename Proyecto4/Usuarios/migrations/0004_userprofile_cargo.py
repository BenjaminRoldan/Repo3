# Generated by Django 4.0.2 on 2022-05-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cargo',
            field=models.CharField(choices=[('Docente', 'Docente'), ('Preceptor', 'Preceptor'), ('Recursos Humanos', 'Recursos Humanos')], max_length=20, null=True),
        ),
    ]
