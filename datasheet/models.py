from django.db import models

# Create your models here.
class TbTipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo_usuario


class TbDatosGeneralesUsuario(models.Model):
    direccion = models.CharField(max_length=70, null=True)
    numero_inscripcion = models.CharField(max_length=4, unique=True, null=True)
    barrio = models.CharField(max_length=70, null=True)
    clave_catastral_actual = models.CharField(max_length=15, unique=True)
    esta_registrado = models.BooleanField(default=False, null=True)

# fix type of data
class TbActividadPredio(models.Model):
    actividad_predio = models.CharField(max_length=70)

    def __str__(self):
        return self.actividad_predio

class TbResponsablePredio(models.Model):
    responsable_predio = models.CharField(max_length=70)

    def __str__(self):
        return self.responsable_predio


class TbTipoPredio(models.Model):
    tipo_predio = models.CharField(max_length=70)
    
    def __str__(self):
        return self.tipo_predio

class TbMaterialConstruccion(models.Model):
    material_construccion = models.CharField(max_length=70)

    def __str__(self):
        return self.material_construccion

class TbTipoServicio(models.Model):
    tipo_servicio = models.CharField(max_length=70)

    def __str__(self):
        return self.tipo_servicio

class TbDatosInmueble(models.Model):
    numero_pisos = models.IntegerField(null=True, blank=True) 
    unidades_domestico = models.IntegerField(null=True, blank=True) 
    unidades_publico = models.IntegerField(null=True, blank=True) 
    unidades_comercial = models.IntegerField(null=True, blank=True) 
    unidades_industrial = models.IntegerField(null=True, blank=True) 
    habitada = models.BooleanField(default=False)
    numero_personas = models.IntegerField(null=True, blank=True) 
    numero_familias = models.IntegerField(null=True, blank=True) 
    pozo_artesiano = models.BooleanField(default=False)
    tiene_piscina = models.BooleanField(default=False)
    actividad_predio =  models.ForeignKey(TbActividadPredio, on_delete=models.CASCADE, null=True , blank=True)
    tipo_predio = models.ForeignKey(TbTipoPredio, on_delete=models.CASCADE, null=True, blank=True)
    material_construccion = models.ForeignKey(TbMaterialConstruccion, on_delete=models.CASCADE, null=True, blank=True)
    tipo_servicio = models.ForeignKey(TbTipoServicio, on_delete=models.CASCADE, null=True, blank=True)

class TbCaracteristicasConexion(models.Model):
    caracteristicas_conexion = models.CharField(max_length=70)

    def __str__(self):
        return self.caracteristicas_conexion

class TbDiametroConexion(models.Model):
    diametro_conexion = models.CharField(max_length=40)

    def __str__(self):
        return self.diametro_conexion

class TbMaterialConexion(models.Model):
    material_conexion = models.CharField(max_length=70)

    def __str__(self):
        return self.material_conexion

class TbSituacionConexion(models.Model):
    situacion_conexion = models.CharField(max_length=70)

class TbUbicacionCajagua(models.Model):
    ubicacion_caja_agua = models.CharField(max_length=40)

    def __str__(self):
        return self.ubicacion_caja_agua

class TbMaterialCaja(models.Model):
    material_caja = models.CharField(max_length=40)

    def __str__(self):
        return self.material_caja

class TbEstadoCaja(models.Model):
    estado_caja = models.CharField(max_length=40)

class TbMaterialMarcoTapa(models.Model):
    material_marco_tapa = models.CharField(max_length=70)

    def __str__(self):
        return self.material_marco_tapa

class TbEstadoMArcoTapa(models.Model):
    estado_marco_tapa = models.CharField(max_length=40)
    def __str__(self):
        return self.estado_marco_tapa

class TbAccesorio(models.Model):
    descripcion_accesorio = models.CharField(max_length=60)

class TbDiametroMedidor(models.Model):
    diametro_medidor = models.CharField(max_length=48)
    
    def __str__(self):
        return self.diametro_medidor

opciones_estado_accesorios = [
    [0, "Bueno"],
    [1, "Malo"],
]



class TbDiametroConexionAlc(models.Model):
    diametro_conexion = models.CharField(max_length=60)

    def __str__(self):
        return self.diametro_conexion

class TbMaterialConexionAlc(models.Model): 
    material_conexion = models.CharField(max_length=60)

    def __str__(self):
        return self.material_conexion

class TbSituacionConexionAlc(models.Model): 
    situacion_conexion = models.CharField(max_length=60)

    def __str__(self):
        return self.situacion_conexion

class TbDatosConexionAlcantarillado(models.Model):
    sin_caja_conexion_directa = models.BooleanField(null=True)
    con_caja_sin_medidor = models.BooleanField(null=True)
    con_caja_con_medidor = models.BooleanField(null=True)
    sin_conexion = models.BooleanField(null=True)
    fecha_instalacion = models.DateField(null=True, blank=True)
    diametro_conexion = models.ForeignKey(TbDiametroConexionAlc, on_delete=models.CASCADE, null=True, blank=True)
    material_conexion = models.ForeignKey(TbMaterialConexionAlc, on_delete=models.CASCADE, null=True, blank=True)
    situacion_conexion = models.ForeignKey(TbSituacionConexionAlc, on_delete=models.CASCADE, null=True, blank=True)

class TbUbicacionCajaRD(models.Model):
    ubicacion_caja = models.CharField(max_length=60)

    def __str__(self):
        return self.ubicacion_caja

class TbMaterialCajaRD(models.Model):
    material_caja = models.CharField(max_length=60)

    def __str__(self):
        return self.material_caja

class TbEstadoCajaRD(models.Model):
    estado_caja = models.CharField(max_length=60)

    def __str__(self):
        return self.estado_caja

class TbDatosCajaRegistroDesague(models.Model):
    ubicacion_caja = models.ForeignKey(TbUbicacionCajaRD, on_delete=models.CASCADE, null=True, blank=True)
    material_caja = models.ForeignKey(TbMaterialCajaRD, on_delete=models.CASCADE, null=True, blank=True)
    estado_caja = models.ForeignKey(TbEstadoCajaRD, on_delete=models.CASCADE, null=True, blank=True)
    tiene_descargas_aass_aall = models.BooleanField(null=True)

class TbMaterialTapa(models.Model):
    material_tapa = models.CharField(max_length=72)

    def __str__(self):
        return self.material_tapa

class TbEstadoTapa(models.Model):
    estado_tapa = models.CharField(max_length=60)

    def __str__(self):
        return self.estado_tapa

class TbDatosTapaCajaAlcantarillado(models.Model):
    material_tapa = models.ForeignKey(TbMaterialTapa, on_delete=models.CASCADE, null=True, blank=True)
    estado_tapa = models.ForeignKey(TbEstadoTapa, on_delete=models.CASCADE, null=True, blank=True)

class TbAbastecimientoAguaPotable(models.Model):
    abastecimiento_agua_potable = models.CharField(max_length=60)
    
    def __str__(self):
        return self.abastecimiento_agua_potable

class TbAlmacenamientoAguaPotable(models.Model):
    almacenamiento_agua_potable = models.CharField(max_length=60)

    def __str__(self):
        return self.almacenamiento_agua_potable

class TbSaneamiento(models.Model):
    descripcion_saneamiento = models.CharField(max_length=60)

    def __str__(self):
        return self.descripcion_saneamiento

class TbDatosSinConexionAguaAlcantarillado(models.Model):
    abastecimiento_agua = models.ForeignKey(TbAbastecimientoAguaPotable, on_delete=models.CASCADE, null=True, blank=True)
    almacenamiento_agua = models.ForeignKey(TbAlmacenamientoAguaPotable, on_delete=models.CASCADE, null=True, blank=True)
    numero_horas_abastecimiento = models.IntegerField(null=True, blank=True)
    saneamiento = models.ForeignKey(TbSaneamiento, on_delete=models.CASCADE, null=True, blank=True)

class TbJardinHuerto(models.Model):
    jardin_huerto = models.CharField(max_length=60)

    def __str__(self):
        return self.jardin_huerto

class TbPavimento(models.Model):
    descripcion_pavimento = models.CharField(max_length=60)

    def __str__(self):
        return self.descripcion_pavimento

class TbTipoVereda(models.Model):
    tipo_vereda = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo_vereda

class TbDatosComplementarios(models.Model):
    jardin_huerto = models.ForeignKey(TbJardinHuerto, on_delete=models.CASCADE, null=True, blank=True)
    pavimento = models.ForeignKey(TbPavimento, on_delete=models.CASCADE, null=True, blank=True)
    tipo_vereda = models.ForeignKey(TbTipoVereda, on_delete=models.CASCADE, null=True, blank=True)

class TbRecoleccionBasura(models.Model): 
    tiene_recoleccion_basura_predio = models.BooleanField(null=True)
    clasifica_residuos_domesticos = models.BooleanField(null=True)
    tiene_contenedores_cercanos_predio = models.BooleanField(null=True)
    especifique_numero_cuadras = models.IntegerField(null=True, blank=True)

class TbEstadoAcometidaAlcantarillado(models.Model):
    estado_acometida_alcantarillado = models.CharField(max_length=60)

class TbFichaTecnica(models.Model):
    numero_ficha = models.CharField(max_length=9)
    observaciones = models.CharField(max_length=255, null=True)
    tercera_edad = models.BooleanField(null=True)
    tiene_carne_conadis = models.BooleanField(null=True)
    fecha_encuesta = models.DateField(null=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True )
    tercera_edad = models.BooleanField(null=True, blank=True)
    tiene_carne_conadis = models.BooleanField(null=True, blank=True)
    fecha_encuesta = models.DateField(null=True, blank=True)
    tipo_usuario = models.ForeignKey(TbTipoUsuario, on_delete=models.CASCADE, null=True)
    datos_generales_usuario = models.ForeignKey(TbDatosGeneralesUsuario, on_delete=models.CASCADE, null=True)
    responsable_predio = models.ForeignKey(TbResponsablePredio, on_delete=models.CASCADE, null=True)
    datos_inmueble = models.ForeignKey(TbDatosInmueble, on_delete=models.CASCADE, null=True)
    datos_conexion_alcantarillado = models.ForeignKey(TbDatosConexionAlcantarillado, on_delete=models.CASCADE, null=True)
    datos_caja_registro_desague = models.ForeignKey(TbDatosCajaRegistroDesague, on_delete=models.CASCADE, null=True)
    datos_tapa_caja_alcantarillado = models.ForeignKey(TbDatosTapaCajaAlcantarillado, on_delete=models.CASCADE, null=True)
    datos_sin_conexion_agua_alc = models.ForeignKey(TbDatosSinConexionAguaAlcantarillado, on_delete=models.CASCADE, null=True)
    datos_complementarios = models.ForeignKey(TbDatosComplementarios, on_delete=models.CASCADE, null=True)
    recoleccion_basura = models.ForeignKey(TbRecoleccionBasura, on_delete=models.CASCADE, null=True)
    estado_acometida_alcantarillado = models.ForeignKey(TbEstadoAcometidaAlcantarillado, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.numero_ficha

class TbDatosResponsableAcometida(models.Model):
    cedula_identidad = models.CharField(max_length=13)
    nombres_apellidos = models.CharField(max_length=70, null=True)

class TbDatosConexionAguaPotable(models.Model):
    fecha_instalacion = models.DateField(null=True)
    caracteristicas_conexion = models.ForeignKey(TbCaracteristicasConexion, on_delete=models.CASCADE)
    diametro_conexion = models.ForeignKey(TbDiametroConexion, on_delete=models.CASCADE, null=True)
    material_conexion = models.ForeignKey(TbMaterialConexion, on_delete=models.CASCADE, null=True)
    situacion_conexion = models.ForeignKey(TbSituacionConexion, on_delete=models.CASCADE, null=True)

class TbDatosCajaAgua(models.Model):
    ubicacion_caja_agua = models.ForeignKey(TbUbicacionCajagua, on_delete=models.CASCADE, null=True)
    material_caja = models.ForeignKey(TbMaterialCaja, on_delete=models.CASCADE, null=True)
    estado_caja = models.ForeignKey(TbEstadoCaja, on_delete=models.CASCADE, null=True)

class TbDatosMarcoTapaCajaAgua(models.Model):
    material_marco_tapa = models.ForeignKey(TbMaterialMarcoTapa, on_delete=models.CASCADE, null=True)
    estado_marco_tapa = models.ForeignKey(TbEstadoMArcoTapa, on_delete=models.CASCADE, null=True)

class TbDatosMedidor(models.Model):
    numero_medidor = models.IntegerField(null=True, blank=True)
    lectura = models.CharField(max_length=45, null=True, blank=True) 
    marca_medidor = models.CharField(max_length=120, null=True, blank=True)
    no_determinado = models.BooleanField(null=True)
    operativo = models.BooleanField(null=True)
    luna_opaca = models.BooleanField(null=True)
    luna_rota = models.BooleanField(null=True)
    sin_tapa = models.BooleanField(null=True)
    malogrado = models.BooleanField(null=True)
    estado_niple_estandar = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    estado_llave_paso = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    estado_directo = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    estado_codo = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    estado_tubo_salida = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    estado_tubo_entrada = models.IntegerField(choices=opciones_estado_accesorios, null=True, blank=True)
    diametro_medidor = models.ForeignKey(TbDiametroMedidor, on_delete=models.CASCADE, null=True, blank=True)

class TbMedidorAccesorio(models.Model):
    datos_medidor = models.ForeignKey(TbDatosMedidor, on_delete=models.CASCADE, null=True)
    accesorio = models.ForeignKey(TbAccesorio, on_delete=models.CASCADE, null=True)
    estado_accesorio = models.BooleanField(null=True) 

class TbEstadoAcometidaAgua(models.Model):
    estado_acometida_agua = models.CharField(max_length=60)


class TbNuevoCodigoCatastral(models.Model):
    provincia = models.IntegerField()
    canton = models.IntegerField()
    parroquia = models.IntegerField()
    zona = models.IntegerField()
    sector = models.IntegerField()
    manzana = models.IntegerField()
    predio = models.IntegerField()
    conexion = models.IntegerField()
    fichatecnica = models.ForeignKey(TbFichaTecnica, on_delete=models.CASCADE, null=True)
    responsableacometida = models.ForeignKey(TbDatosResponsableAcometida, on_delete=models.CASCADE, null=True)
    datos_conexion_agua_potable =  models.ForeignKey(TbDatosConexionAguaPotable, on_delete=models.CASCADE, null=True)
    datos_caja_agua =  models.ForeignKey(TbDatosCajaAgua, on_delete=models.CASCADE, null=True)
    datos_marco_tapa_caja_agua =  models.ForeignKey(TbDatosMarcoTapaCajaAgua, on_delete=models.CASCADE, null=True)
    datos_medidor=  models.ForeignKey(TbDatosMedidor, on_delete=models.CASCADE, null=True)
    estado_acometida_agua=  models.ForeignKey(TbEstadoAcometidaAgua, on_delete=models.CASCADE, null=True)
