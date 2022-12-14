# Generated by Django 3.2.15 on 2022-11-09 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0013_alter_tbnuevocodigocatastral_conexion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_codo',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_directo',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_llave_paso',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_niple_estandar',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_tubo_entrada',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_tubo_salida',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='tbdatoscajaagua',
            name='estado_caja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadocaja'),
        ),
        migrations.AlterField(
            model_name='tbdatoscajaagua',
            name='material_caja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialcaja'),
        ),
        migrations.AlterField(
            model_name='tbdatoscajaagua',
            name='ubicacion_caja_agua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbubicacioncajagua'),
        ),
        migrations.AlterField(
            model_name='tbdatosconexionaguapotable',
            name='caracteristicas_conexion',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbcaracteristicasconexion'),
        ),
        migrations.AlterField(
            model_name='tbdatosconexionaguapotable',
            name='diametro_conexion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdiametroconexion'),
        ),
        migrations.AlterField(
            model_name='tbdatosconexionaguapotable',
            name='fecha_instalacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosconexionaguapotable',
            name='material_conexion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialconexion'),
        ),
        migrations.AlterField(
            model_name='tbdatosconexionaguapotable',
            name='situacion_conexion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbsituacionconexion'),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='actividad_predio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbactividadpredio'),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='material_construccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialconstruccion'),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='numero_familias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='numero_personas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='numero_pisos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='tipo_predio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtipopredio'),
        ),
        migrations.AlterField(
            model_name='tbdatosinmueble',
            name='tipo_servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtiposervicio'),
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
        migrations.AlterField(
            model_name='tbdatosmarcotapacajaagua',
            name='estado_marco_tapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadomarcotapa'),
        ),
        migrations.AlterField(
            model_name='tbdatosmarcotapacajaagua',
            name='material_marco_tapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialmarcotapa'),
        ),
        migrations.AlterField(
            model_name='tbfichatecnica',
            name='responsable_predio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbresponsablepredio'),
        ),
        migrations.AlterField(
            model_name='tbnuevocodigocatastral',
            name='conexion',
            field=models.IntegerField(),
        ),
    ]
