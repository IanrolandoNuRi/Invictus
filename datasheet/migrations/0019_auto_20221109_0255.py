# Generated by Django 3.2.12 on 2022-11-09 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0018_auto_20221109_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbfichatecnica',
            name='datos_caja_agua',
        ),
        migrations.RemoveField(
            model_name='tbfichatecnica',
            name='datos_conexion_agua_potable',
        ),
        migrations.RemoveField(
            model_name='tbfichatecnica',
            name='datos_marco_tapa_caja_agua',
        ),
        migrations.RemoveField(
            model_name='tbfichatecnica',
            name='datos_medidor',
        ),
        migrations.AddField(
            model_name='tbdatoscajaagua',
            name='fichatecnica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbfichatecnica'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionaguapotable',
            name='fichatecnica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbfichatecnica'),
        ),
        migrations.AddField(
            model_name='tbdatosmarcotapacajaagua',
            name='fichatecnica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbfichatecnica'),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='fichatecnica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbfichatecnica'),
        ),
    ]
