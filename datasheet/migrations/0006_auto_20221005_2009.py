# Generated by Django 3.2.12 on 2022-10-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0005_auto_20221005_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbfichatecnica',
            name='tercera_edad',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbfichatecnica',
            name='tiene_carne_conadis',
            field=models.BooleanField(null=True),
        ),
    ]
