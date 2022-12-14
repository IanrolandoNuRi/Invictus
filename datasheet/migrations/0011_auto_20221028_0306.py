# Generated by Django 3.2.12 on 2022-10-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0010_auto_20221007_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='numero_pisos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='unidades_comercial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='unidades_domestico',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='unidades_industrial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='unidades_publico',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
