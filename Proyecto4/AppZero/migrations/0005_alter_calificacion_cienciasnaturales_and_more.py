# Generated by Django 4.0.2 on 2022-05-18 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0004_nota_remove_calificacion_alumno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='cienciasnaturales',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='cienciassociales',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='educacionfisica',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='ingles',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='matematicas',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
    ]
