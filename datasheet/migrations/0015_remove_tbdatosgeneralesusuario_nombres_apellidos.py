# Generated by Django 3.2.12 on 2022-11-08 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0014_remove_tbdatosgeneralesusuario_cedula_identidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbdatosgeneralesusuario',
            name='nombres_apellidos',
        ),
    ]