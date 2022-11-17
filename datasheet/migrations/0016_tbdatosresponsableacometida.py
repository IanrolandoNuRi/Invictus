# Generated by Django 3.2.12 on 2022-11-08 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0015_remove_tbdatosgeneralesusuario_nombres_apellidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbDatosResponsableAcometida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_identidad', models.CharField(max_length=13)),
                ('nombres_apellidos', models.CharField(max_length=70, null=True)),
                ('nuevocodigocatastral', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbnuevocodigocatastral')),
            ],
        ),
    ]