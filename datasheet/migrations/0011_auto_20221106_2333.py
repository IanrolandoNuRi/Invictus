# Generated by Django 3.2.16 on 2022-11-07 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0010_auto_20221007_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbfichatecnica',
            name='responsable_predio',
        ),
        migrations.AddField(
            model_name='tbfichatecnica',
            name='responsable_predio_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbresponsablepredio'),
        ),
    ]
