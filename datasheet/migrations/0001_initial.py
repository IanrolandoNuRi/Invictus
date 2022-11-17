# Generated by Django 3.2.12 on 2022-10-03 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbAbastecimientoAguaPotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abastecimiento_agua_potable', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbAccesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_accesorio', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbActividadPredio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad_predio', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbAlmacenamientoAguaPotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacenamiento_agua_potable', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbCaracteristicasConexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas_conexion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbCaracteristicasConexionAlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristica_conexion', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosCajaAgua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosCajaRegistroDesague',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiene_descargas_aass_aall', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosComplementarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosConexionAguaPotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField(null=True)),
                ('caracteristicas_conexion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbcaracteristicasconexion')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosConexionAlcantarillado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField(null=True)),
                ('caracteristica_conexion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbcaracteristicasconexionalc')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosGeneralesUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_identidad', models.CharField(max_length=13, unique=True)),
                ('nombres', models.CharField(max_length=70, null=True)),
                ('apellidos', models.CharField(max_length=70, null=True)),
                ('direccion', models.CharField(max_length=70, null=True)),
                ('numero_inscripcion', models.CharField(max_length=4, null=True, unique=True)),
                ('barrio', models.CharField(max_length=70, null=True)),
                ('clave_catastral_actual', models.CharField(max_length=15, unique=True)),
                ('esta_registrado', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_pisos', models.IntegerField(null=True)),
                ('habitada', models.BooleanField(default=False)),
                ('numero_personas', models.IntegerField(null=True)),
                ('numero_familias', models.IntegerField(null=True)),
                ('pozo_artesiano', models.BooleanField(default=False)),
                ('tiene_piscina', models.BooleanField(default=False)),
                ('actividad_predio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbactividadpredio')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosMarcoTapaCajaAgua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosMedidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_medidor', models.IntegerField(null=True)),
                ('lectura', models.CharField(max_length=45, null=True)),
                ('marca_medidor', models.CharField(max_length=120, null=True)),
                ('no_determinado', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosSinConexionAguaAlcantarillado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_horas_abastecimiento', models.IntegerField(null=True)),
                ('abastecimiento_agua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbabastecimientoaguapotable')),
                ('almacenamiento_agua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbalmacenamientoaguapotable')),
            ],
        ),
        migrations.CreateModel(
            name='TbDatosTapaCajaAlcantarillado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TbDiametroConexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametro_conexion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbDiametroConexionAlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametro_conexion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbDiametroMedidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametro_medidor', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='TbEstadoCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_caja', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbEstadoCajaRD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_caja', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbEstadoMArcoTapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_marco_tapa', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbEstadoMedidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_medidor', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TbEstadoTapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_tapa', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbJardinHuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jardin_huerto', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_caja', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialCajaRD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_caja', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialConexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_conexion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialConexionAlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_conexion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialConstruccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_construccion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialMarcoTapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_marco_tapa', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbMaterialTapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_tapa', models.CharField(max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='TbNuevoCodigoCatastral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=2)),
                ('canton', models.CharField(max_length=2)),
                ('parroquia', models.CharField(max_length=2)),
                ('zona', models.CharField(max_length=2)),
                ('sector', models.CharField(max_length=2)),
                ('manzana', models.CharField(max_length=2)),
                ('predio', models.CharField(max_length=2)),
                ('conexion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TbPavimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_pavimento', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbRecoleccionBasura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiene_recoleccion_basura_predio', models.BooleanField(null=True)),
                ('clasifica_residuos_domesticos', models.BooleanField(null=True)),
                ('tiene_contenedores_cercanos_predio', models.BooleanField(null=True)),
                ('especifique_numero_cuadras', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TbResponsablePredio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable_predio', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbSaneamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_saneamiento', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbSituacionConexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacion_conexion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbSituacionConexionAlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacion_conexion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbTipoPredio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_predio', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbTipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbTipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbTipoVereda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vereda', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbUbicacionCajagua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_caja_agua', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TbUbicacionCajaRD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_caja', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TbUnidadesUso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades_uso', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TbMedidorAccesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_accesorio', models.BooleanField(null=True)),
                ('accesorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbaccesorio')),
                ('datos_medidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosmedidor')),
            ],
        ),
        migrations.CreateModel(
            name='TbFichaTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ficha', models.CharField(max_length=9)),
                ('observaciones', models.CharField(max_length=255, null=True)),
                ('fecha_encuesta', models.DateField(null=True)),
                ('datos_caja_agua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatoscajaagua')),
                ('datos_caja_registro_desague', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatoscajaregistrodesague')),
                ('datos_complementarios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatoscomplementarios')),
                ('datos_conexion_agua_potable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosconexionaguapotable')),
                ('datos_conexion_alcantarillado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosconexionalcantarillado')),
                ('datos_generales_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosgeneralesusuario')),
                ('datos_inmueble', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosinmueble')),
                ('datos_marco_tapa_caja_agua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosmarcotapacajaagua')),
                ('datos_medidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatosmedidor')),
                ('datos_sin_conexion_agua_alc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatossinconexionaguaalcantarillado')),
                ('datos_tapa_caja_alcantarillado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdatostapacajaalcantarillado')),
                ('nuevo_codigo_catastral', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbnuevocodigocatastral')),
                ('recoleccion_basura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbrecoleccionbasura')),
                ('responsable_predio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbresponsablepredio')),
                ('tipo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtipousuario')),
            ],
        ),
        migrations.AddField(
            model_name='tbdatostapacajaalcantarillado',
            name='estado_tapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadotapa'),
        ),
        migrations.AddField(
            model_name='tbdatostapacajaalcantarillado',
            name='material_tapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialtapa'),
        ),
        migrations.AddField(
            model_name='tbdatossinconexionaguaalcantarillado',
            name='saneamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbsaneamiento'),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='diametro_medidor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdiametromedidor'),
        ),
        migrations.AddField(
            model_name='tbdatosmedidor',
            name='estado_medidor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadomedidor'),
        ),
        migrations.AddField(
            model_name='tbdatosmarcotapacajaagua',
            name='estado_marco_tapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadomarcotapa'),
        ),
        migrations.AddField(
            model_name='tbdatosmarcotapacajaagua',
            name='material_marco_tapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialmarcotapa'),
        ),
        migrations.AddField(
            model_name='tbdatosinmueble',
            name='material_construccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialconstruccion'),
        ),
        migrations.AddField(
            model_name='tbdatosinmueble',
            name='tipo_predio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtipopredio'),
        ),
        migrations.AddField(
            model_name='tbdatosinmueble',
            name='tipo_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtiposervicio'),
        ),
        migrations.AddField(
            model_name='tbdatosinmueble',
            name='unidades_uso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbunidadesuso'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionalcantarillado',
            name='diametro_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdiametroconexionalc'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionalcantarillado',
            name='material_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialconexionalc'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionalcantarillado',
            name='situacion_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbsituacionconexionalc'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionaguapotable',
            name='diametro_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbdiametroconexion'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionaguapotable',
            name='material_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialconexion'),
        ),
        migrations.AddField(
            model_name='tbdatosconexionaguapotable',
            name='situacion_conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbsituacionconexion'),
        ),
        migrations.AddField(
            model_name='tbdatoscomplementarios',
            name='jardin_huerto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbjardinhuerto'),
        ),
        migrations.AddField(
            model_name='tbdatoscomplementarios',
            name='pavimento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbpavimento'),
        ),
        migrations.AddField(
            model_name='tbdatoscomplementarios',
            name='tipo_vereda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbtipovereda'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaregistrodesague',
            name='estado_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadocajard'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaregistrodesague',
            name='material_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialcajard'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaregistrodesague',
            name='ubicacion_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbubicacioncajard'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaagua',
            name='estado_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbestadocaja'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaagua',
            name='material_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbmaterialcaja'),
        ),
        migrations.AddField(
            model_name='tbdatoscajaagua',
            name='ubicacion_caja_agua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasheet.tbubicacioncajagua'),
        ),
    ]