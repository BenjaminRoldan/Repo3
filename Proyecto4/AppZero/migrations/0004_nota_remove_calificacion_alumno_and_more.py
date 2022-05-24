# Generated by Django 4.0.2 on 2022-05-18 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppZero', '0003_alumno_email_autoridad_email_docente_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C1', models.FloatField(blank=True, null=True)),
                ('C2', models.FloatField(blank=True, null=True)),
                ('C3', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='nota',
        ),
        migrations.AddField(
            model_name='alumno',
            name='calificaciones',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppZero.calificacion'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppZero.docente'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='cienciasnaturales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='cienciassociales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='educacionfisica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='ingles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='matematicas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='AppZero.nota'),
        ),
    ]