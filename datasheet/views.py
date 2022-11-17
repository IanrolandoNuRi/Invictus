import json
from itertools import chain
from email import header
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .static import constants
from .models import TbAbastecimientoAguaPotable, TbAccesorio, TbActividadPredio, TbAlmacenamientoAguaPotable, TbCaracteristicasConexion, TbDatosCajaAgua, TbDatosCajaRegistroDesague, TbDatosComplementarios, TbDatosConexionAguaPotable, TbDatosConexionAlcantarillado, TbDatosGeneralesUsuario, TbDatosInmueble, TbDatosMarcoTapaCajaAgua, TbDatosMedidor, TbDatosSinConexionAguaAlcantarillado, TbDatosTapaCajaAlcantarillado, TbDiametroConexion, TbDiametroConexionAlc, TbDiametroMedidor, TbEstadoCaja, TbEstadoCajaRD, TbEstadoMArcoTapa, TbEstadoTapa, TbFichaTecnica, TbJardinHuerto, TbMaterialCaja, TbMaterialCajaRD, TbMaterialConexion, TbMaterialConexionAlc, TbMaterialConstruccion, TbMaterialMarcoTapa, TbMaterialTapa, TbMedidorAccesorio, TbNuevoCodigoCatastral, TbPavimento, TbRecoleccionBasura, TbResponsablePredio, TbSaneamiento, TbSituacionConexion, TbSituacionConexionAlc, TbTipoPredio, TbTipoServicio, TbTipoUsuario, TbTipoVereda, TbUbicacionCajaRD, TbUbicacionCajagua, TbDatosResponsableAcometida
from .forms import TbDatosGeneralesUsuarioForm, TbNuevoCodigoCatastralForm, TbFichaTecnicaForm, TbDatosInmuebleForm, TbDatosConexionAguaPotableForm, TbDatosCajaAguaForm, TbDatosMarcoTapaCajaAguaForm, TbDatosMedidorForm, TbDatosConexionAlcantarilladoForm, TbDatosCajaRegistroDesagueForm, TbDatosTapaCajaAlcantarilladoForm, TbDatosSinConexionAguaAlcantarilladoForm, TbDatosComplementariosForm, TbRecoleccionBasuraForm

# Create your views here.
def Home(request):
  print(request.GET)
  return render(request, 'index.html')

def ViewDataSheet(request):
    tipo_usuarios= TbTipoUsuario.objects.all()
    predio_responsables= TbResponsablePredio.objects.all()
    tipo_predios = TbTipoPredio.objects.all()
    construccion_materiales = TbMaterialConstruccion.objects.all()
    servicio_tipos = TbTipoServicio.objects.all()
    predio_actividades = TbActividadPredio.objects.all()
    conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
    conexion_diametros = TbDiametroConexion.objects.all()
    conexion_materiales = TbMaterialConexion.objects.all()
    conexion_situaciones = TbSituacionConexion.objects.all()
    caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
    caja_materiales = TbMaterialCaja.objects.all()
    caja_estados = TbEstadoCaja.objects.all()
    marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
    marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
    medidor_diametros= TbDiametroMedidor.objects.all()
    accesorios= TbAccesorio.objects.all()
    alc_conexion_diametros= TbDiametroConexionAlc.objects.all()
    alc_conexion_materiales= TbMaterialConexionAlc.objects.all()
    alc_conexion_situaciones= TbSituacionConexionAlc.objects.all()
    caja_residual_ubicaciones= TbUbicacionCajaRD.objects.all()
    caja_residual_materiales= TbMaterialCajaRD.objects.all()
    caja_residual_estados= TbEstadoCajaRD.objects.all()
    tapa_materiales= TbMaterialTapa.objects.all()
    tapa_estados= TbEstadoTapa.objects.all()
    agua_potable_abastecimientos= TbAbastecimientoAguaPotable.objects.all()
    agua_potable_almacenamientos= TbAlmacenamientoAguaPotable.objects.all()
    saneamientos= TbSaneamiento.objects.all()
    jardin_huerto_tipos= TbJardinHuerto.objects.all()
    vereda_tipos= TbTipoVereda.objects.all()
    pavimentos= TbPavimento.objects.all()

    tb_nuevo_codigo_catastral= TbNuevoCodigoCatastral.objects.get(id=1)
    allData = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    datos_generales= TbDatosGeneralesUsuario.objects.get(id=allData.datos_generales_usuario_id)
    datos_inmueble= TbDatosInmueble.objects.get(id=allData.datos_inmueble_id)
    datos_agua_potable= TbDatosConexionAguaPotable.objects.get(id=tb_nuevo_codigo_catastral.datos_conexion_agua_potable_id)
    fecha_conexion_agua_potable= datos_agua_potable.fecha_instalacion.strftime("%Y-%m-%d") if datos_agua_potable.fecha_instalacion else ""
    datos_caja_agua= TbDatosCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_caja_agua_id)
    datos_marco_tapa_caja_agua= TbDatosMarcoTapaCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_marco_tapa_caja_agua_id)
    datos_medidor= TbDatosMedidor.objects.get(id=tb_nuevo_codigo_catastral.datos_medidor_id)
    medidor_accesorios= TbMedidorAccesorio.objects.filter(datos_medidor_id=tb_nuevo_codigo_catastral.datos_medidor_id)
    datos_conexion_alcantarillado= TbDatosConexionAlcantarillado.objects.get(id=allData.datos_conexion_alcantarillado_id)
    fecha_conexion_alcantarillado=  datos_conexion_alcantarillado.fecha_instalacion.strftime("%Y-%m-%d") if datos_conexion_alcantarillado.fecha_instalacion else ""
    datos_caja_registro_desague= TbDatosCajaRegistroDesague.objects.get(id=allData.datos_caja_registro_desague_id)
    datos_tapa_caja_alcantarillado= TbDatosTapaCajaAlcantarillado.objects.get(id=allData.datos_tapa_caja_alcantarillado_id)
    datos_sin_conexion_agua_alcantarillado= TbDatosSinConexionAguaAlcantarillado.objects.get(id=allData.datos_sin_conexion_agua_alc_id)
    datos_complementarios= TbDatosComplementarios.objects.get(id=allData.datos_complementarios_id)
    recoleccion_basura= TbRecoleccionBasura.objects.get(id=allData.recoleccion_basura_id)
    fecha_encuesta=  allData.fecha_encuesta.strftime("%Y-%m-%d") if allData.fecha_encuesta else ""

    context={
      'header': constants.title_ficha_catastral,
      'has_edit_permission': True,
      'edit_mode': False,

      'tipo_usuarios': tipo_usuarios,
      'predio_responsables': predio_responsables,
      'tipo_predios': tipo_predios,
      'construccion_materiales': construccion_materiales,
      'servicio_tipos': servicio_tipos,
      'predio_actividades': predio_actividades,
      'conexion_caracteristicas': conexion_caracteristicas,
      'conexion_diametros': conexion_diametros,
      'conexion_materiales': conexion_materiales,
      'conexion_situaciones': conexion_situaciones,
      'caja_agua_ubicaciones': caja_agua_ubicaciones,
      'caja_materiales': caja_materiales,
      'caja_estados': caja_estados,
      'marco_tapa_materiales': marco_tapa_materiales,
      'marco_tapa_estados': marco_tapa_estados,
      'medidor_diametros': medidor_diametros,
      'accesorios': accesorios,
      'alc_conexion_diametros': alc_conexion_diametros,
      'alc_conexion_materiales': alc_conexion_materiales,
      'alc_conexion_situaciones': alc_conexion_situaciones,
      'caja_residual_ubicaciones': caja_residual_ubicaciones,
      'caja_residual_materiales': caja_residual_materiales,
      'caja_residual_estados': caja_residual_estados,
      'tapa_materiales': tapa_materiales,
      'tapa_estados': tapa_estados,
      'agua_potable_abastecimientos': agua_potable_abastecimientos,
      'agua_potable_almacenamientos': agua_potable_almacenamientos,
      'saneamientos': saneamientos,
      'jardin_huerto_tipos': jardin_huerto_tipos,
      'vereda_tipos': vereda_tipos,
      'pavimentos': pavimentos,

      # 'data':allData,
      # 'nuevo_cod_catastral': nuevo_cod_catastral,
      # 'datos_generales': datos_generales,
      # 'datos_inmueble': datos_inmueble,
      # 'datos_agua_potable': datos_agua_potable,
      # 'fecha_conexion_agua_potable': fecha_conexion_agua_potable,
      # 'datos_caja_agua': datos_caja_agua,
      # 'datos_marco_tapa_caja_agua': datos_marco_tapa_caja_agua,
      # 'datos_medidor': datos_medidor,
      # 'medidor_accesorio': medidor_accesorio,
      # 'datos_conexion_alcantarillado': datos_conexion_alcantarillado,
      # 'fecha_conexion_alcantarillado': fecha_conexion_alcantarillado,
      # 'datos_caja_registro_desague': datos_caja_registro_desague,
      # 'datos_tapa_caja_alcantarillado': datos_tapa_caja_alcantarillado,
      # 'datos_sin_conexion_agua_alcantarillado': datos_sin_conexion_agua_alcantarillado,
      # 'datos_complementarios': datos_complementarios,
      # 'recoleccion_basura': recoleccion_basura,
      # 'fecha_encuesta': fecha_encuesta,
    }
    return render(request, 'view_datasheet.html', context)


def CoordinacionAgua(request, num):
  if request.method == 'GET': 
    tipo_usuarios= TbTipoUsuario.objects.all()
    predio_responsables= TbResponsablePredio.objects.all()
    tipo_predios = TbTipoPredio.objects.all()
    construccion_materiales = TbMaterialConstruccion.objects.all()
    servicio_tipos = TbTipoServicio.objects.all()
    predio_actividades = TbActividadPredio.objects.all()
    conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
    conexion_diametros = TbDiametroConexion.objects.all()
    conexion_materiales = TbMaterialConexion.objects.all()
    conexion_situaciones = TbSituacionConexion.objects.all()
    caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
    caja_materiales = TbMaterialCaja.objects.all()
    caja_estados = TbEstadoCaja.objects.all()
    marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
    marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
    medidor_diametros= TbDiametroMedidor.objects.all()
    accesorios= TbAccesorio.objects.all()
    jardin_huerto_tipos= TbJardinHuerto.objects.all()
    vereda_tipos= TbTipoVereda.objects.all()
    pavimentos= TbPavimento.objects.all()


    tb_nuevo_codigo_catastral= TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    datos_generales= TbDatosGeneralesUsuario.objects.get(id=tb_ficha_tecnica.datos_generales_usuario_id)
    datos_inmueble= TbDatosInmueble.objects.get(id=tb_ficha_tecnica.datos_inmueble_id)
    datos_agua_potable= TbDatosConexionAguaPotable.objects.get(id=tb_nuevo_codigo_catastral.datos_conexion_agua_potable_id)
    fecha_conexion_agua_potable= datos_agua_potable.fecha_instalacion.strftime("%Y-%m-%d") if datos_agua_potable.fecha_instalacion else ""
    datos_caja_agua= TbDatosCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_caja_agua_id)
    datos_marco_tapa_caja_agua= TbDatosMarcoTapaCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_marco_tapa_caja_agua_id)
    datos_medidor= TbDatosMedidor.objects.get(id=tb_nuevo_codigo_catastral.datos_medidor_id)
    medidor_accesorios= TbMedidorAccesorio.objects.filter(datos_medidor_id=tb_nuevo_codigo_catastral.datos_medidor_id)
    estado_acometida= TbEstadoAcometidaAgua.objects.get(id=tb_nuevo_codigo_catastral.estado_acometida_agua_id)

    datos_complementarios= TbDatosComplementarios.objects.get(id=tb_ficha_tecnica.datos_complementarios_id)


    context={
      'header': constants.title_coordinacion_agua,
      'has_edit_permission': True,
      'edit_mode': False,

      'tipo_usuarios': tipo_usuarios,
      'predio_responsables': predio_responsables,
      'tipo_predios': tipo_predios,
      'construccion_materiales': construccion_materiales,
      'servicio_tipos': servicio_tipos,
      'predio_actividades': predio_actividades,
      'conexion_caracteristicas': conexion_caracteristicas,
      'conexion_diametros': conexion_diametros,
      'conexion_materiales': conexion_materiales,
      'conexion_situaciones': conexion_situaciones,
      'caja_agua_ubicaciones': caja_agua_ubicaciones,
      'caja_materiales': caja_materiales,
      'caja_estados': caja_estados,
      'marco_tapa_materiales': marco_tapa_materiales,
      'marco_tapa_estados': marco_tapa_estados,
      'medidor_diametros': medidor_diametros,
      'accesorios': accesorios,
      'jardin_huerto_tipos': jardin_huerto_tipos,
      'vereda_tipos': vereda_tipos,
      'pavimentos': pavimentos,
      
      'data':tb_ficha_tecnica,
      'nuevo_cod_catastral': tb_nuevo_codigo_catastral,
      'datos_generales': datos_generales,
      'datos_responsableacometida': datos_responsableacometida,
      'datos_inmueble': datos_inmueble,
      'datos_agua_potable': datos_agua_potable,
      'fecha_conexion_agua_potable': fecha_conexion_agua_potable,
      'datos_caja_agua': datos_caja_agua,
      'datos_marco_tapa_caja_agua': datos_marco_tapa_caja_agua,
      'datos_medidor': datos_medidor,
      'medidor_accesorios': medidor_accesorios,
      'datos_complementarios': datos_complementarios,
      'estado_acometida': estado_acometida,
    }

    return render(request, 'coordinaciones/coord_agua.html', context)
  else:

    tb_nuevo_codigo_catastral = TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    tb_datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    tb_datos_generales = TbDatosGeneralesUsuario.objects.get(id=tb_ficha_tecnica.datos_generales_usuario_id)
    tb_datos_inmueble = TbDatosInmueble.objects.get(id=tb_ficha_tecnica.datos_inmueble_id)
    tb_datos_conexion_ap = TbDatosConexionAguaPotable.objects.get(id=tb_nuevo_codigo_catastral.datos_conexion_agua_potable_id)
    tb_datos_marco_tapa_ca = TbDatosMarcoTapaCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_marco_tapa_caja_agua_id)
    tb_datos_medidor = TbDatosMedidor.objects.get(id=tb_nuevo_codigo_catastral.datos_medidor_id)
    ipt_accesorio_ids, estado_accesorios= getDatosMedidorAccesorio(request)
    tb_datos_complementarios = TbDatosComplementarios.objects.get(id=tb_ficha_tecnica.datos_complementarios_id)

    updateDatosResponsableAcometida(getDatosResponsableAcometida(request), tb_datos_responsableacometida)
    updateDatosGenerales(getDatosGenerales(request), tb_datos_generales)
    updateNuevoCodigoCatastral(getNuevoCodigoCatastral(request), tb_nuevo_codigo_catastral)
    updateDatosInmueble(getDatosInmueble(request), tb_datos_inmueble)
    updateDatosConexionAP(getDatosConexionAP(request), tb_datos_conexion_ap)
    updateDatosMarcoTapaCA(getDatosMarcoTapaCA(request), tb_datos_marco_tapa_ca)
    updateDatosMedidor(getDatosMedidor(request), tb_datos_medidor)
    updateDatosMedidorAccesorio(ipt_accesorio_ids=ipt_accesorio_ids, estado_accesorios=estado_accesorios, medidor_id=tb_datos_medidor.id)
    updateDatosComplementarios(getDatosComplementarios(request), tb_datos_complementarios)
    updateFichaTecnica(getFichaTecnica(request, True, False, False), tb_ficha_tecnica)

    return render(request, 'coordinaciones/coord_agua.html')

def NuevaAcometida(request, num):
  if request.method == 'GET': 
    tipo_usuarios= TbTipoUsuario.objects.all()
    predio_responsables= TbResponsablePredio.objects.all()
    tipo_predios = TbTipoPredio.objects.all()
    construccion_materiales = TbMaterialConstruccion.objects.all()
    servicio_tipos = TbTipoServicio.objects.all()
    predio_actividades = TbActividadPredio.objects.all()
    conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
    conexion_diametros = TbDiametroConexion.objects.all()
    conexion_materiales = TbMaterialConexion.objects.all()
    conexion_situaciones = TbSituacionConexion.objects.all()
    caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
    caja_materiales = TbMaterialCaja.objects.all()
    caja_estados = TbEstadoCaja.objects.all()
    marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
    marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
    medidor_diametros= TbDiametroMedidor.objects.all()
    accesorios= TbAccesorio.objects.all()
    jardin_huerto_tipos= TbJardinHuerto.objects.all()
    vereda_tipos= TbTipoVereda.objects.all()
    pavimentos= TbPavimento.objects.all()


    tb_nuevo_codigo_catastral= TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    datos_generales= TbDatosGeneralesUsuario.objects.get(id=tb_ficha_tecnica.datos_generales_usuario_id)
    datos_inmueble= TbDatosInmueble.objects.get(id=tb_ficha_tecnica.datos_inmueble_id)
    datos_agua_potable= TbDatosConexionAguaPotable.objects.get(id=tb_nuevo_codigo_catastral.datos_conexion_agua_potable_id)
    fecha_conexion_agua_potable= datos_agua_potable.fecha_instalacion.strftime("%Y-%m-%d") if datos_agua_potable.fecha_instalacion else ""
    datos_caja_agua= TbDatosCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_caja_agua_id)
    datos_marco_tapa_caja_agua= TbDatosMarcoTapaCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_marco_tapa_caja_agua_id)
    datos_medidor= TbDatosMedidor.objects.get(id=tb_nuevo_codigo_catastral.datos_medidor_id)
    medidor_accesorios= TbMedidorAccesorio.objects.filter(datos_medidor_id=tb_nuevo_codigo_catastral.datos_medidor_id)

    datos_complementarios= TbDatosComplementarios.objects.get(id=tb_ficha_tecnica.datos_complementarios_id)


    context={
      'header': constants.title_nueva_acometida,
      'has_edit_permission': True,
      'edit_mode': False,

      'tipo_usuarios': tipo_usuarios,
      'predio_responsables': predio_responsables,
      'tipo_predios': tipo_predios,
      'construccion_materiales': construccion_materiales,
      'servicio_tipos': servicio_tipos,
      'predio_actividades': predio_actividades,
      'conexion_caracteristicas': conexion_caracteristicas,
      'conexion_diametros': conexion_diametros,
      'conexion_materiales': conexion_materiales,
      'conexion_situaciones': conexion_situaciones,
      'caja_agua_ubicaciones': caja_agua_ubicaciones,
      'caja_materiales': caja_materiales,
      'caja_estados': caja_estados,
      'marco_tapa_materiales': marco_tapa_materiales,
      'marco_tapa_estados': marco_tapa_estados,
      'medidor_diametros': medidor_diametros,
      'accesorios': accesorios,
      'jardin_huerto_tipos': jardin_huerto_tipos,
      'vereda_tipos': vereda_tipos,
      'pavimentos': pavimentos,
      
      'data':tb_ficha_tecnica,
      'nuevo_cod_catastral': tb_nuevo_codigo_catastral,
      'datos_generales': datos_generales,
      'datos_responsableacometida': datos_responsableacometida,
      'datos_inmueble': datos_inmueble,
      'datos_agua_potable': datos_agua_potable,
      'fecha_conexion_agua_potable': fecha_conexion_agua_potable,
      'datos_caja_agua': datos_caja_agua,
      'datos_marco_tapa_caja_agua': datos_marco_tapa_caja_agua,
      'datos_medidor': datos_medidor,
      'medidor_accesorios': medidor_accesorios,
      'datos_complementarios': datos_complementarios,
    }

    return render(request, 'coordinaciones/nueva_acometida.html', context)
    
  else:

    tb_nuevo_codigo_catastral = TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    tb_datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    tb_datos_conexion_ap = TbDatosConexionAguaPotable.objects.get(id=tb_nuevo_codigo_catastral.datos_conexion_agua_potable_id)
    tb_datos_marco_tapa_ca = TbDatosMarcoTapaCajaAgua.objects.get(id=tb_nuevo_codigo_catastral.datos_marco_tapa_caja_agua_id)
    tb_datos_medidor = TbDatosMedidor.objects.get(id=tb_nuevo_codigo_catastral.datos_medidor_id)

    foreign_data = {
      'tb_ficha_tecnica':tb_ficha_tecnica,
      'tb_datos_responsableacometida':saveDatosResponsableAcometida(request),
      'tb_datos_conexion_ap':saveDatosConexionAP(request),
      'tb_datos_marco_tapa_ca':saveDatosMarcoTapaCA(request),
      'tb_datos_medidor': saveDatosMedidor(request),
      'tb_caja_agua': saveDatosCajaAguaAcometida(request)
    }
    
    
    saveDatosMedidorAccesorio(request, medidor_id=tb_datos_medidor.id)
    saveNuevoCodigoCatastral(request, foreign_data)


    return render(request, 'coordinaciones/nueva_acometida.html')
  

def CoordinacionDesechosSolidos(request, num):
  if request.method == 'GET': 
    tipo_usuarios= TbTipoUsuario.objects.all()
    predio_responsables= TbResponsablePredio.objects.all()
    tipo_predios = TbTipoPredio.objects.all()
    construccion_materiales = TbMaterialConstruccion.objects.all()
    servicio_tipos = TbTipoServicio.objects.all()
    predio_actividades = TbActividadPredio.objects.all()
    conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
    conexion_diametros = TbDiametroConexion.objects.all()
    conexion_materiales = TbMaterialConexion.objects.all()
    conexion_situaciones = TbSituacionConexion.objects.all()
    caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
    caja_materiales = TbMaterialCaja.objects.all()
    caja_estados = TbEstadoCaja.objects.all()
    marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
    marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
    medidor_diametros= TbDiametroMedidor.objects.all()
    accesorios= TbAccesorio.objects.all()
    alc_conexion_diametros= TbDiametroConexionAlc.objects.all()
    alc_conexion_materiales= TbMaterialConexionAlc.objects.all()
    alc_conexion_situaciones= TbSituacionConexionAlc.objects.all()
    caja_residual_ubicaciones= TbUbicacionCajaRD.objects.all()
    caja_residual_materiales= TbMaterialCajaRD.objects.all()
    caja_residual_estados= TbEstadoCajaRD.objects.all()
    tapa_materiales= TbMaterialTapa.objects.all()
    tapa_estados= TbEstadoTapa.objects.all()
    agua_potable_abastecimientos= TbAbastecimientoAguaPotable.objects.all()
    agua_potable_almacenamientos= TbAlmacenamientoAguaPotable.objects.all()
    saneamientos= TbSaneamiento.objects.all()
    jardin_huerto_tipos= TbJardinHuerto.objects.all()
    vereda_tipos= TbTipoVereda.objects.all()
    pavimentos= TbPavimento.objects.all()

    tb_nuevo_codigo_catastral= TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    datos_generales= TbDatosGeneralesUsuario.objects.get(id=tb_ficha_tecnica.datos_generales_usuario_id)
    datos_inmueble= TbDatosInmueble.objects.get(id=tb_ficha_tecnica.datos_inmueble_id)
    recoleccion_basura= TbRecoleccionBasura.objects.get(id=tb_ficha_tecnica.recoleccion_basura_id)

    context={
      'header': constants.title_coordinacion_desechos_solidos,
      'has_edit_permission': True,
      'edit_mode': False,

      'tipo_usuarios': tipo_usuarios,
      'predio_responsables': predio_responsables,
      'tipo_predios': tipo_predios,
      'construccion_materiales': construccion_materiales,
      'servicio_tipos': servicio_tipos,
      'predio_actividades': predio_actividades,
      'conexion_caracteristicas': conexion_caracteristicas,
      'conexion_diametros': conexion_diametros,
      'conexion_materiales': conexion_materiales,
      'conexion_situaciones': conexion_situaciones,
      'caja_agua_ubicaciones': caja_agua_ubicaciones,
      'caja_materiales': caja_materiales,
      'caja_estados': caja_estados,
      'marco_tapa_materiales': marco_tapa_materiales,
      'marco_tapa_estados': marco_tapa_estados,
      'medidor_diametros': medidor_diametros,
      'accesorios': accesorios,
      'alc_conexion_diametros': alc_conexion_diametros,
      'alc_conexion_materiales': alc_conexion_materiales,
      'alc_conexion_situaciones': alc_conexion_situaciones,
      'caja_residual_ubicaciones': caja_residual_ubicaciones,
      'caja_residual_materiales': caja_residual_materiales,
      'caja_residual_estados': caja_residual_estados,
      'tapa_materiales': tapa_materiales,
      'tapa_estados': tapa_estados,
      'agua_potable_abastecimientos': agua_potable_abastecimientos,
      'agua_potable_almacenamientos': agua_potable_almacenamientos,
      'saneamientos': saneamientos,
      'jardin_huerto_tipos': jardin_huerto_tipos,
      'vereda_tipos': vereda_tipos,
      'pavimentos': pavimentos,
      
      'data':tb_ficha_tecnica,
      'nuevo_cod_catastral': tb_nuevo_codigo_catastral,
      'datos_responsableacometida': datos_responsableacometida,
      'datos_generales': datos_generales,
      'nuevo_cod_catastral': tb_nuevo_codigo_catastral,
      'datos_inmueble': datos_inmueble,
      'recoleccion_basura': recoleccion_basura,
    }
    return render(request, 'coordinaciones/coord_desechos.html', context)
  else:

    tb_nuevo_codigo_catastral= TbNuevoCodigoCatastral.objects.get(id=num)

    tb_ficha_tecnica = TbFichaTecnica.objects.get(id=tb_nuevo_codigo_catastral.fichatecnica_id)
    tb_datos_responsableacometida= TbDatosResponsableAcometida.objects.get(id=tb_nuevo_codigo_catastral.responsableacometida_id)
    tb_datos_generales = TbDatosGeneralesUsuario.objects.get(id=tb_ficha_tecnica.datos_generales_usuario_id)
    tb_datos_inmueble = TbDatosInmueble.objects.get(id=tb_ficha_tecnica.datos_inmueble_id)
    tb_datos_recoleccion_basura = TbRecoleccionBasura.objects.get(id=tb_ficha_tecnica.recoleccion_basura_id)
    
    updateDatosResponsableAcometida(getDatosResponsableAcometida(request), tb_datos_responsableacometida)
    updateDatosGenerales(getDatosGenerales(request), tb_datos_generales)
    updateNuevoCodigoCatastral(getNuevoCodigoCatastral(request), tb_nuevo_codigo_catastral)
    updateDatosInmueble(getDatosInmueble(request), tb_datos_inmueble)
    updateRecoleccionBasura(getRecoleccionBasura(request), tb_datos_recoleccion_basura)
    updateFichaTecnica(getFichaTecnica(request, False, False, True), tb_ficha_tecnica)

    return render(request, 'coordinaciones/coord_desechos.html')
  
    

def CoordinacionAlcantarillado(request):
  if request.method == 'GET':
    conditions = {
      'header': constants.title_coordinacion_alcantarillado,
      'has_edit_permission': True,
      'edit_mode': True,
      'mode': 'save'
    }
    context = Data(conditions)
    return render(request, 'coordinaciones/coord_alc.html', context);

class ListarFicha(ListView):
  model = TbFichaTecnica

  def get_queryset(self):
    fichas = self.model.objects.all()
    result = []
    i= 0 
    for ficha in fichas:
      datos_generales = TbDatosGeneralesUsuario.objects.get(id=ficha.datos_generales_usuario_id)
      n_cod = TbNuevoCodigoCatastral.objects.get(id=ficha.nuevo_codigo_catastral_id)
      nuevo_codigo = str(n_cod.provincia) + str(n_cod.canton) + str(n_cod.parroquia) + str(n_cod.zona) + str(n_cod.sector) + str(n_cod.manzana) + str(n_cod.predio) + str(n_cod.conexion)
      result.append({
        "id" : str(ficha.id),
        "numero_ficha" : str(ficha.numero_ficha),
        "observaciones": str(ficha.observaciones),
        "fecha_encuesta": str(ficha.fecha_encuesta),
        "cedula_identidad": str(datos_generales.cedula_identidad),
        "clave_catastral_actual": str(datos_generales.clave_catastral_actual),
        "nuevo_codigo_catastral": str(nuevo_codigo),
      })
    return result
  
  def get(self, request, *args, **kwargs):
    if request.is_ajax():
      return HttpResponse(json.dumps(self.get_queryset()), content_type='application/json')
    else:
      return redirect('ficha:inicio_fichas')

class CreateDataSheet(CreateView):
  template_name = 'view_datasheet.html'
  form_class = TbDatosGeneralesUsuarioForm
  form_class2 = TbNuevoCodigoCatastralForm
  form_class3 = TbFichaTecnicaForm
  form_class4 = TbDatosInmuebleForm
  form_class5 = TbDatosConexionAguaPotableForm
  form_class6 = TbDatosCajaAguaForm
  form_class7 = TbDatosMarcoTapaCajaAguaForm
  form_class8 = TbDatosMedidorForm
  form_class9 = TbDatosConexionAlcantarilladoForm
  form_class10 = TbDatosCajaRegistroDesagueForm
  form_class11 = TbDatosTapaCajaAlcantarilladoForm
  form_class12 = TbDatosSinConexionAguaAlcantarilladoForm
  form_class13 = TbDatosComplementariosForm
  form_class14 = TbRecoleccionBasuraForm
  success_url = reverse_lazy('ficha:listar_fichas')

  def get(self, request, *args, **kwargs):
    return render(request, self.template_name, {'form': self.form_class, 'form2': self.form_class2, 'form3': self.form_class3, 'form4': self.form_class4,
                                                'form5': self.form_class5, 'form6': self.form_class6, 'form7': self.form_class7, 'form8': self.form_class8,
                                                'form9': self.form_class9, 'form10': self.form_class10, 'form11': self.form_class11, 'form12': self.form_class12,
                                                'form13': self.form_class13, 'form14': self.form_class14,
                                                'has_edit_permission':True, 'header': constants.title_ficha_catastral})

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)  # TbDatosGeneralesUsuarioForm
    form2 = self.form_class2(request.POST) # TbNuevoCodigoCatastralForm
    form3 = self.form_class3(request.POST) # TbFichaTecnicaForm
    form4 = self.form_class4(request.POST) # TbDatosInmuebleForm
    form5 = self.form_class5(request.POST) # TbDatosConexionAguaPotableForm
    form6 = self.form_class6(request.POST) # TbDatosCajaAguaForm
    form7 = self.form_class7(request.POST) # TbDatosMarcoTapaCajaAguaForm
    form8 = self.form_class8(request.POST) # TbDatosMedidorForm
    form9 = self.form_class9(request.POST) # TbDatosConexionAlcantarilladoForm
    form10 = self.form_class10(request.POST) # TbDatosCajaRegistroDesagueForm
    form11 = self.form_class11(request.POST) # TbDatosTapaCajaAlcantarilladoForm
    form12 = self.form_class12(request.POST) # TbDatosSinConexionAguaAlcantarilladoForm
    form13 = self.form_class13(request.POST) # TbDatosComplementariosForm
    form14 = self.form_class14(request.POST) # TbRecoleccionBasuraForm
    if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid() and form11.is_valid() and form12.is_valid() and form13.is_valid() and form14.is_valid() :
      form.save(commit=False)
      form2.save(commit=False)
      form4.save(commit=False)
      form5.save(commit=False)
      form6.save(commit=False)
      form7.save(commit=False)
      form8.save(commit=False)
      form9.save(commit=False)
      form10.save(commit=False)
      form11.save(commit=False)
      form12.save(commit=False)
      form13.save(commit=False)
      form14.save(commit=False)
      ficha_tecnica = form3.save(commit=False)
      ficha_tecnica.datos_generales_usuario = form.save()
      ficha_tecnica.nuevo_codigo_catastral = form2.save()
      ficha_tecnica.datos_inmueble = form4.save()
      ficha_tecnica.datos_conexion_agua_potable = form5.save()
      ficha_tecnica.datos_caja_agua = form6.save()
      ficha_tecnica.datos_marco_tapa_caja_agua = form7.save()
      ficha_tecnica.datos_medidor = form8.save()
      ficha_tecnica.datos_conexion_alcantarillado = form9.save()
      ficha_tecnica.datos_caja_registro_desague = form10.save()
      ficha_tecnica.datos_tapa_caja_alcantarillado = form11.save()
      ficha_tecnica.datos_sin_conexion_agua_alc = form12.save()
      ficha_tecnica.datos_complementarios = form13.save()
      ficha_tecnica.recoleccion_basura = form14.save()
      ficha_tecnica.save()
      messages.success(request, "Ficha creada correctamente")
      return redirect(self.success_url)
    else:
      form = self.form_class(request.POST)
      form2 = self.form_class2(request.POST)
      form3 = self.form_class3(request.POST)
      form4 = self.form_class4(request.POST)
      form5 = self.form_class5(request.POST)
      form6 = self.form_class6(request.POST)
      form7 = self.form_class7(request.POST)
      form8 = self.form_class8(request.POST)
      form9 = self.form_class9(request.POST)
      form10 = self.form_class10(request.POST)
      form11 = self.form_class11(request.POST)
      form12 = self.form_class12(request.POST)
      form13 = self.form_class13(request.POST)
      form14 = self.form_class14(request.POST)
      return render(request, self.template_name, {'form': form, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8,
                                                  'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 'form13': form13, 'form14': form14,
                                                  'has_edit_permission':True})

def EditDataSheet(request, pk):
  template_name = 'edit_datasheet.html'
  form_class = None
  fc_datos_generales = None
  fc_nuevo_codigo_catastral = None
  fc_datos_inmuebles = None
  fc_datos_conexion_ap = None
  fc_datos_caja_agua = None
  fc_datos_marco_tapa = None
  fc_datos_medidor = None
  fc_datos_con_alc = None
  fc_datos_caja_rd = None
  fc_tapa_caja_alc = None
  fc_datos_scon_aalc = None
  fc_datos_compleme = None
  fc_recoleccion_basu = None
  success_url = reverse_lazy('ficha:listar_fichas')
  error = None

  try:
    inst_ficha = TbFichaTecnica.objects.get(id=pk)
    inst_datos_generales = TbDatosGeneralesUsuario.objects.get(id=inst_ficha.datos_generales_usuario_id)
    inst_nuevo_codigo_catastral = TbNuevoCodigoCatastral.objects.get(id=inst_ficha.nuevo_codigo_catastral_id)
    inst_datos_inmuebles = TbDatosInmueble.objects.get(id=inst_ficha.datos_inmueble_id)
    inst_datos_conexion_ap = TbDatosConexionAguaPotable.objects.get(id=inst_ficha.datos_conexion_agua_potable_id)
    inst_datos_caja_agua = TbDatosCajaAgua.objects.get(id=inst_ficha.datos_caja_agua_id)
    inst_datos_marco_tapa = TbDatosMarcoTapaCajaAgua.objects.get(id=inst_ficha.datos_marco_tapa_caja_agua_id)
    inst_datos_medidor = TbDatosMedidor.objects.get(id=inst_ficha.datos_medidor_id)
    inst_datos_con_alc = TbDatosConexionAlcantarillado.objects.get(id=inst_ficha.datos_conexion_alcantarillado_id)
    inst_datos_caja_rd = TbDatosCajaRegistroDesague.objects.get(id=inst_ficha.datos_caja_registro_desague_id)
    inst_tapa_caja_alc = TbDatosTapaCajaAlcantarillado.objects.get(id=inst_ficha.datos_tapa_caja_alcantarillado_id)
    inst_datos_scon_aalc = TbDatosSinConexionAguaAlcantarillado.objects.get(id=inst_ficha.datos_sin_conexion_agua_alc_id)
    inst_datos_compleme = TbDatosComplementarios.objects.get(id=inst_ficha.datos_complementarios_id)
    inst_recoleccion_basu = TbRecoleccionBasura.objects.get(id=inst_ficha.recoleccion_basura_id)
    if request.method == 'GET':
      form_class = TbFichaTecnicaForm(instance=inst_ficha)
      fc_datos_generales = TbDatosGeneralesUsuarioForm(instance=inst_datos_generales)
      fc_nuevo_codigo_catastral = TbNuevoCodigoCatastralForm(instance=inst_nuevo_codigo_catastral)
      fc_datos_inmuebles = TbDatosInmuebleForm(instance=inst_datos_inmuebles)
      fc_datos_conexion_ap = TbDatosConexionAguaPotableForm(instance=inst_datos_conexion_ap)
      fc_datos_caja_agua = TbDatosCajaAguaForm(instance=inst_datos_caja_agua)
      fc_datos_marco_tapa = TbDatosMarcoTapaCajaAguaForm(instance=inst_datos_marco_tapa)
      fc_datos_medidor = TbDatosMedidorForm(instance=inst_datos_medidor)
      fc_datos_con_alc = TbDatosConexionAlcantarilladoForm(instance=inst_datos_con_alc)
      fc_datos_caja_rd = TbDatosCajaRegistroDesagueForm(instance=inst_datos_caja_rd)
      fc_tapa_caja_alc = TbDatosTapaCajaAlcantarilladoForm(instance=inst_tapa_caja_alc)
      fc_datos_scon_aalc = TbDatosSinConexionAguaAlcantarilladoForm(instance=inst_datos_scon_aalc)
      fc_datos_compleme = TbDatosComplementariosForm(instance=inst_datos_compleme)
      fc_recoleccion_basu = TbRecoleccionBasuraForm(instance=inst_recoleccion_basu)
    else:
      form_class = TbFichaTecnicaForm(request.POST, instance=inst_ficha)
      fc_datos_generales = TbDatosGeneralesUsuarioForm(request.POST, instance=inst_datos_generales)
      fc_nuevo_codigo_catastral = TbNuevoCodigoCatastralForm(request.POST, instance=inst_nuevo_codigo_catastral)
      fc_datos_inmuebles = TbDatosInmuebleForm(request.POST, instance=inst_datos_inmuebles)
      fc_datos_conexion_ap = TbDatosConexionAguaPotableForm(request.POST, instance=inst_datos_conexion_ap)
      fc_datos_caja_agua = TbDatosCajaAguaForm(request.POST, instance=inst_datos_caja_agua)
      fc_datos_marco_tapa = TbDatosMarcoTapaCajaAguaForm(request.POST, instance=inst_datos_marco_tapa)
      fc_datos_medidor = TbDatosMedidorForm(request.POST, instance=inst_datos_medidor)
      fc_datos_con_alc = TbDatosConexionAlcantarilladoForm(request.POST, instance=inst_datos_con_alc)
      fc_datos_caja_rd = TbDatosCajaRegistroDesagueForm(request.POST, instance=inst_datos_caja_rd)
      fc_tapa_caja_alc = TbDatosTapaCajaAlcantarilladoForm(request.POST, instance=inst_tapa_caja_alc)
      fc_datos_scon_aalc = TbDatosSinConexionAguaAlcantarilladoForm(request.POST, instance=inst_datos_scon_aalc)
      fc_datos_compleme = TbDatosComplementariosForm(request.POST, instance=inst_datos_compleme)
      fc_recoleccion_basu = TbRecoleccionBasuraForm(request.POST, instance=inst_recoleccion_basu)
      if form_class.is_valid() and fc_datos_generales.is_valid() and fc_nuevo_codigo_catastral.is_valid() and fc_datos_inmuebles.is_valid() and fc_datos_conexion_ap.is_valid() and fc_datos_caja_agua.is_valid() and fc_datos_marco_tapa.is_valid() and fc_datos_medidor.is_valid() and fc_datos_con_alc.is_valid() and fc_datos_caja_rd.is_valid() and fc_tapa_caja_alc.is_valid() and fc_datos_scon_aalc.is_valid() and fc_datos_compleme.is_valid() and fc_recoleccion_basu.is_valid():
        form_class.save()
        fc_datos_generales.save()
        fc_nuevo_codigo_catastral.save()
        fc_datos_inmuebles.save()
        fc_datos_conexion_ap.save()
        fc_datos_caja_agua.save()
        fc_datos_marco_tapa.save()
        fc_datos_medidor.save()
        fc_datos_con_alc.save()
        fc_datos_caja_rd.save()
        fc_tapa_caja_alc.save()
        fc_datos_scon_aalc.save()
        fc_datos_compleme.save()
        fc_recoleccion_basu.save()
        messages.success(request, "Ficha editada correctamente")
        return redirect(success_url)
  except ObjectDoesNotExist as e:
      error = e
  return render(request, template_name, {'form': fc_datos_generales, 'form2': fc_nuevo_codigo_catastral, 'form3': form_class, 'form4': fc_datos_inmuebles,
                                                'form5': fc_datos_conexion_ap, 'form6': fc_datos_caja_agua, 'form7': fc_datos_marco_tapa, 'form8': fc_datos_medidor,
                                                'form9': fc_datos_con_alc, 'form10': fc_datos_caja_rd, 'form11': fc_tapa_caja_alc, 'form12': fc_datos_scon_aalc,
                                                'form13': fc_datos_compleme, 'form14': fc_recoleccion_basu,
                                                'has_edit_permission': True, 'header': constants.title_ficha_catastral})

class DeleteDataSheet(DeleteView):
  model = TbFichaTecnica
  success_url = reverse_lazy('ficha:listar_fichas')
  template_name = 'tbfichatecnica_confirm_delete.html'
  error = None

  def delete(self,request,*args,**kwargs):
    if request.is_ajax():
      inst_ficha = TbFichaTecnica.objects.get(id=kwargs['pk'])
      inst_datos_generales = TbDatosGeneralesUsuario.objects.get(id=inst_ficha.datos_generales_usuario_id)
      inst_nuevo_codigo_catastral = TbNuevoCodigoCatastral.objects.get(id=inst_ficha.nuevo_codigo_catastral_id)
      inst_datos_inmuebles = TbDatosInmueble.objects.get(id=inst_ficha.datos_inmueble_id)
      inst_datos_conexion_ap = TbDatosConexionAguaPotable.objects.get(id=inst_ficha.datos_conexion_agua_potable_id)
      inst_datos_caja_agua = TbDatosCajaAgua.objects.get(id=inst_ficha.datos_caja_agua_id)
      inst_datos_marco_tapa = TbDatosMarcoTapaCajaAgua.objects.get(id=inst_ficha.datos_marco_tapa_caja_agua_id)
      inst_datos_medidor = TbDatosMedidor.objects.get(id=inst_ficha.datos_medidor_id)
      inst_datos_con_alc = TbDatosConexionAlcantarillado.objects.get(id=inst_ficha.datos_conexion_alcantarillado_id)
      inst_datos_caja_rd = TbDatosCajaRegistroDesague.objects.get(id=inst_ficha.datos_caja_registro_desague_id)
      inst_tapa_caja_alc = TbDatosTapaCajaAlcantarillado.objects.get(id=inst_ficha.datos_tapa_caja_alcantarillado_id)
      inst_datos_scon_aalc = TbDatosSinConexionAguaAlcantarillado.objects.get(id=inst_ficha.datos_sin_conexion_agua_alc_id)
      inst_datos_compleme = TbDatosComplementarios.objects.get(id=inst_ficha.datos_complementarios_id)
      inst_recoleccion_basu = TbRecoleccionBasura.objects.get(id=inst_ficha.recoleccion_basura_id)
      inst_datos_generales.delete()
      inst_nuevo_codigo_catastral.delete()
      inst_datos_inmuebles.delete()
      inst_datos_conexion_ap.delete()
      inst_datos_caja_agua.delete()
      inst_datos_marco_tapa.delete()
      inst_datos_medidor.delete()
      inst_datos_con_alc.delete()
      inst_datos_caja_rd.delete()
      inst_tapa_caja_alc.delete()
      inst_datos_scon_aalc.delete()
      inst_datos_compleme.delete()
      inst_recoleccion_basu.delete()
      inst_ficha.delete()
      # messages.success(request, "Ficha eliminada correctamente")
      # return redirect(self.success_url)
      mensaje = 'Eliminado correctamente!'
      error = 'No hay error!'
      response = JsonResponse({'mensaje': mensaje, 'error': error})
      response.status_code = 201
      return response
    return redirect(self.success_url)

# def Data(conditions):
#   tipo_usuarios= TbTipoUsuario.objects.all()
#   predio_responsables= TbResponsablePredio.objects.all()
#   tipo_predios = TbTipoPredio.objects.all()
#   construccion_materiales = TbMaterialConstruccion.objects.all()
#   servicio_tipos = TbTipoServicio.objects.all()
#   predio_actividades = TbActividadPredio.objects.all()
#   conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
#   conexion_diametros = TbDiametroConexion.objects.all()
#   conexion_materiales = TbMaterialConexion.objects.all()
#   conexion_situaciones = TbSituacionConexion.objects.all()
#   caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
#   caja_materiales = TbMaterialCaja.objects.all()
#   caja_estados = TbEstadoCaja.objects.all()
#   marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
#   marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
#   medidor_diametros= TbDiametroMedidor.objects.all()
#   accesorios= TbAccesorio.objects.all()
#   alc_conexion_diametros= TbDiametroConexionAlc.objects.all()
#   alc_conexion_materiales= TbMaterialConexionAlc.objects.all()
#   alc_conexion_situaciones= TbSituacionConexionAlc.objects.all()
#   caja_residual_ubicaciones= TbUbicacionCajaRD.objects.all()
#   caja_residual_materiales= TbMaterialCajaRD.objects.all()
#   caja_residual_estados= TbEstadoCajaRD.objects.all()
#   tapa_materiales= TbMaterialTapa.objects.all()
#   tapa_estados= TbEstadoTapa.objects.all()
#   agua_potable_abastecimientos= TbAbastecimientoAguaPotable.objects.all()
#   agua_potable_almacenamientos= TbAlmacenamientoAguaPotable.objects.all()
#   saneamientos= TbSaneamiento.objects.all()
#   jardin_huerto_tipos= TbJardinHuerto.objects.all()
#   vereda_tipos= TbTipoVereda.objects.all()
#   pavimentos= TbPavimento.objects.all()

#   context={
#     'header': conditions['header'],
#     'has_edit_permission': conditions['has_edit_permission'],
#     'edit_mode': conditions['edit_mode'],
#     'mode': conditions['mode'],

#     'tipo_usuarios': tipo_usuarios,
#     'predio_responsables': predio_responsables,
#     'tipo_predios': tipo_predios,
#     'construccion_materiales': construccion_materiales,
#     'servicio_tipos': servicio_tipos,
#     'predio_actividades': predio_actividades,
#     'conexion_caracteristicas': conexion_caracteristicas,
#     'conexion_diametros': conexion_diametros,
#     'conexion_materiales': conexion_materiales,
#     'conexion_situaciones': conexion_situaciones,
#     'caja_agua_ubicaciones': caja_agua_ubicaciones,
#     'caja_materiales': caja_materiales,
#     'caja_estados': caja_estados,
#     'marco_tapa_materiales': marco_tapa_materiales,
#     'marco_tapa_estados': marco_tapa_estados,
#     'medidor_diametros': medidor_diametros,
#     'accesorios': accesorios,
#     'alc_conexion_diametros': alc_conexion_diametros,
#     'alc_conexion_materiales': alc_conexion_materiales,
#     'alc_conexion_situaciones': alc_conexion_situaciones,
#     'caja_residual_ubicaciones': caja_residual_ubicaciones,
#     'caja_residual_materiales': caja_residual_materiales,
#     'caja_residual_estados': caja_residual_estados,
#     'tapa_materiales': tapa_materiales,
#     'tapa_estados': tapa_estados,
#     'agua_potable_abastecimientos': agua_potable_abastecimientos,
#     'agua_potable_almacenamientos': agua_potable_almacenamientos,
#     'saneamientos': saneamientos,
#     'jardin_huerto_tipos': jardin_huerto_tipos,
#     'vereda_tipos': vereda_tipos,
#     'pavimentos': pavimentos,
#   }
#   return context
# def CreateDataSheet(request):
#   if request.method == 'GET': 
#     conditions = {
#       'header': constants.title_ficha_catastral,
#       'has_edit_permission': True,
#       'edit_mode': True,
#       'mode': 'save'
#     }
#     context = Data(conditions)
#     return render(request, 'view_datasheet.html', context)
#   else:   
#     tb_datos_generales = TbDatosGeneralesUsuario(
#       cedula_identidad=request.POST['ipt_ci_ruc'],
#       nombres_apellidos=request.POST['ipt_nombres_apellidos'],
#       direccion=request.POST['ipt_direccion'],
#       numero_inscripcion=request.POST['ipt_num_inscripcion'],
#       barrio=request.POST['ipt_lugar'],
#       clave_catastral_actual=request.POST['ipt_codigo_actual'],
#       esta_registrado=request.POST["rdo_esta_registrado"],
#     )
#     tb_datos_generales.save()

#     tb_nuevo_codigo_catastral = TbNuevoCodigoCatastral(
#       provincia = request.POST['ipt_provincia'],
#       canton = request.POST['ipt_canton'],
#       parroquia = request.POST['ipt_parroquia'],
#       zona = request.POST['ipt_zona'],
#       sector = request.POST['ipt_sector'],
#       manzana = request.POST['ipt_manzana'],
#       predio = request.POST['ipt_predio'],
#       conexion = request.POST['ipt_conexion']
#     )
#     tb_nuevo_codigo_catastral.save()

#     tb_datos_inmueble = TbDatosInmueble(
#       numero_pisos = request.POST['ipt_numero_pisos'], 
#       unidades_domestico = request.POST['ipt_uu_domestico'],
#       unidades_publico = request.POST['ipt_uu_publico'],
#       unidades_comercial = request.POST['ipt_uu_comercial'], 
#       unidades_industrial = request.POST['ipt_uu_industrial'],
#       habitada = request.POST['rdo_habitada'],
#       numero_personas = request.POST['ipt_numero_personas'],
#       numero_familias = request.POST['ipt_numero_familias'], 
#       pozo_artesiano = request.POST['rdo_pozo_artesiano'],
#       tiene_piscina = request.POST['rdo_piscina'],
#       actividad_predio_id = request.POST['slc_actividad_predio'],
#       tipo_predio_id = request.POST['slc_tipo_predio'],
#       material_construccion_id = request.POST['slc_material_construccion'],
#       tipo_servicio_id = request.POST['slc_tipo_servicio']
#     )
#     tb_datos_inmueble.save()

#     tb_datos_conexion_ap = TbDatosConexionAguaPotable(
#       fecha_instalacion = request.POST['ipt_fecha_instalacion'],
#       caracteristicas_conexion_id = request.POST['slc_caracteristica_conexion_ap'],
#       diametro_conexion_id = request.POST['slc_diametro_conexion_ap'],
#       material_conexion_id = request.POST['slc_material_conexion_ap'],
#       situacion_conexion_id = request.POST['slc_situacion_conexion_ap']
#     )
#     tb_datos_conexion_ap.save()
    
#     tb_datos_caja_agua = TbDatosCajaAgua(
#       ubicacion_caja_agua_id = request.POST['slc_ubicacion_caja'],
#       material_caja_id = request.POST['slc_material_caja'],
#       estado_caja_id = request.POST['slc_estado_caja']
#     )
#     tb_datos_caja_agua.save()

#     tb_datos_marco_tapa_ca = TbDatosMarcoTapaCajaAgua(
#       material_marco_tapa_id =  request.POST['slc_material_marco_tapa'],
#       estado_marco_tapa_id =  request.POST['slc_estado_marco_tapa'],
#     )
#     tb_datos_marco_tapa_ca.save()

#     tb_datos_medidor = TbDatosMedidor(
#       numero_medidor = request.POST['ipt_numero_medidor'],
#       lectura = request.POST['ipt_lectura'],
#       marca_medidor = request.POST['ipt_marca_medidor'],
#       no_determinado = request.POST.get('cek_nodeterminado', False),
#       operativo = request.POST.get('ipt_datos_medidor_operativo', False),
#       luna_opaca = request.POST.get('ipt_datos_medidor_luna_opaca', False),
#       luna_rota = request.POST.get('ipt_datos_medidor_luna_rota', False),
#       sin_tapa = request.POST.get('ipt_datos_medidor_sin_tapa', False),
#       malogrado = request.POST.get('ipt_datos_medidor_malogrado', False),
#       diametro_medidor_id = request.POST['slc_diametro_medidor']
#     )
#     tb_datos_medidor.save()

#     #TODO
#     ipt_accesorio_ids = request.POST.getlist('ipt_accesorio_id')
#     estado_accesorios = request.POST.getlist('slc_estado_accesorio')
#     i=0
#     for accesorio_id in ipt_accesorio_ids:
#       print("Hola" + accesorio_id)
#       tb_medidor_accesorio = TbMedidorAccesorio(
#         datos_medidor_id = tb_datos_medidor.id, 
#         accesorio_id = accesorio_id,
#         estado_accesorio = estado_accesorios[i]
#       )
#       tb_medidor_accesorio.save()
#       i=i+1

#     tb_datos_conexion_alcantarillado = TbDatosConexionAlcantarillado(
#       sin_caja_conexion_directa = request.POST.get('ipt_sin_caja_conexion_directa', False),
#       con_caja_sin_medidor = request.POST.get('ipt_con_caja_sin_medidor', False),
#       con_caja_con_medidor = request.POST.get('ipt_con_caja_con_medidor', False),
#       sin_conexion = request.POST.get('ipt_sin_conexion_alc', False),
#       fecha_instalacion = request.POST['ipt_fecha_instalacion_alc'],
#       diametro_conexion_id = request.POST['slc_diametro_conexion_alc'],
#       material_conexion_id = request.POST['slc_material_conexion_alc'],
#       situacion_conexion_id = request.POST['slc_situacion_conexion_alc']
#     )
#     tb_datos_conexion_alcantarillado.save()

#     tb_datos_caja_registro_desague = TbDatosCajaRegistroDesague(
#       ubicacion_caja_id = request.POST['slc_ubicacion_caja_rd'],
#       material_caja_id = request.POST['slc_material_caja_rd'],
#       estado_caja_id = request.POST['slc_estado_caja_rd'],
#       tiene_descargas_aass_aall = request.POST['rdo_descargas_asss_all']
#     )
#     tb_datos_caja_registro_desague.save()

#     tb_datos_tapa_caja_alcantarillado = TbDatosTapaCajaAlcantarillado(
#       material_tapa_id = request.POST['slc_material_tapa'],
#       estado_tapa_id = request.POST['slc_estado_tapa']
#     )
#     tb_datos_tapa_caja_alcantarillado.save()

#     tb_datos_sin_conexion_agua_alc = TbDatosSinConexionAguaAlcantarillado(
#       abastecimiento_agua_id = request.POST['slc_abastecimiento_agua'],
#       almacenamiento_agua_id = request.POST['slc_almacenamiento_agua'],
#       numero_horas_abastecimiento = request.POST['ipt_horas_abastecimi'],
#       saneamiento_id = request.POST['slc_saneamiento']
#     ) 
#     tb_datos_sin_conexion_agua_alc.save()

#     tb_datos_complementarios = TbDatosComplsaveDatosCajaAguaAcometidaementarios(
#       jardin_huerto_id = request.POST['slc_jardin_huerto'],
#       pavimento_id = request.POST['slc_pavimento'],
#       tipo_vereda_id = request.POST['slc_tipo_vereda']
#     )
#     tb_datos_complementarios.save()

#     tb_recoleccion_basura = TbRecoleccionBasura(
#       tiene_recoleccion_basura_predio = request.POST['rdo_tiene_recoleccion'],
#       clasifica_residuos_domesticos = request.POST['rdo_clasifica_residuos'],
#       tiene_contenedores_cercanos_predio = request.POST['rdo_contenedores_cercanos'],
#       especifique_numero_cuadras = request.POST['ipt_numero_cuadras']
#     )
#     tb_recoleccion_basura.save()

#     tb_ficha_tecnica = TbFichaTecnica(
#       numero_ficha = request.POST['ipt_numero_ficha'],
#       tipo_usuario_id = request.POST['slc_tipo_usuario'],
#       datos_generales_usuario_id = tb_datos_generales.id,
#       nuevo_codigo_catastral_id = tb_nuevo_codigo_catastral.id,
#       responsable_predio_id = request.POST['rdo_responsable_predio'],
#       datos_inmueble_id = tb_datos_inmueble.id,
#       datos_conexion_agua_potable_id = tb_datos_conexion_ap.id,
#       datos_caja_agua_id = tb_datos_caja_agua.id,
#       datos_marco_tapa_caja_agua_id = tb_datos_marco_tapa_ca.id, 
#       datos_medidor_id = tb_datos_medidor.id, 
#       datos_conexion_alcantarillado_id = tb_datos_conexion_alcantarillado.id, 
#       datos_caja_registro_desague_id = tb_datos_caja_registro_desague.id, 
#       datos_tapa_caja_alcantarillado_id = tb_datos_tapa_caja_alcantarillado.id,
#       datos_sin_conexion_agua_alc_id = tb_datos_sin_conexion_agua_alc.id, 
#       datos_complementarios_id = tb_datos_complementarios.id, 
#       recoleccion_basura_id = tb_recoleccion_basura.id, 
#       observaciones = request.POST['txa_observaciones'],
#       tercera_edad = request.POST['rdo_tercera_edad'],
#       tiene_carne_conadis = request.POST['rdo_carne_conadis'],
#       fecha_encuesta = request.POST['ipt_fecha_encuesta']
#     )
#     tb_ficha_tecnica.save()
#     print("Datos guardados con éxito")

#     return redirect('/create-datasheet/')


def saveNewData(request):
  tb_datos_generales = getDatosGenerales(request)
  tb_nuevo_codigo_catastral = getNuevoCodigoCatastral(request)
  tb_datos_inmueble = getDatosInmueble(request)
  tb_datos_conexion_ap = getDatosConexionAP(request)
  tb_datos_caja_agua = getDatosCajaAgua(request)
  tb_datos_marco_tapa_ca = getDatosMarcoTapaCA(request)
  tb_datos_medidor = getDatosMedidor(request)
  ipt_accesorio_ids = getDatosMedidorAccesorio(request)
  tb_datos_conexion_alcantarillado = getDatosConexionAlcantarillado(request)
  tb_datos_caja_registro_desague = getDatosCajaRegistroDesague(request)
  tb_datos_tapa_caja_alcantarillado = getDatosTapaCajaAlcantarillado(request)
  tb_datos_sin_conexion_agua_alc = getDatosSinConexionAguaAlcantarillado(request)
  tb_datos_complementarios = getDatosComplementarios(request)
  tb_recoleccion_basura = getRecoleccionBasura(request)
  
  ##Save all data into db except ficha general table
  # tb_datos_generales.save()
  # tb_nuevo_codigo_catastral.save()

  foreingObjectsIds= {
    "datos_generales_usuario" : tb_datos_generales.id,
    "nuevo_codigo_catastral" : tb_nuevo_codigo_catastral.id,
    "datos_inmueble" : tb_datos_inmueble.id,
    "datos_conexion_agua_potable" : tb_datos_conexion_ap.id,
    "datos_caja_agua" : tb_datos_caja_agua.id,
    "datos_marco_tapa_caja_agua" : tb_datos_marco_tapa_ca.id,
    "datos_medidor" : tb_datos_medidor.id,
    "datos_conexion_alcantarillado" : tb_datos_conexion_alcantarillado.id,
    "datos_caja_registro_desague" : tb_datos_caja_registro_desague.id,
    "datos_tapa_caja_alcantarillado" : tb_datos_tapa_caja_alcantarillado.id,
    "datos_sin_conexion_agua_alc" : tb_datos_sin_conexion_agua_alc.id,
    "datos_complementarios" : tb_datos_complementarios.id,
    "recoleccion_basura" : tb_recoleccion_basura.id,
  }

  tb_ficha_tecnica = getFichaTecnica(request, objectsIds = foreingObjectsIds)
  
  print("here is the general ",tb_datos_generales.__dict__)
  print("here is the catastral ",tb_nuevo_codigo_catastral.__dict__)
  print("here is the inmueble ",tb_datos_inmueble.__dict__)
  print("here is the conexion ap ",tb_datos_conexion_ap.__dict__)
  print("here is the datos caja agua ",tb_datos_caja_agua.__dict__)
  print("here is the datos marco tapa ",tb_datos_marco_tapa_ca.__dict__)
  print("here is the datos medidor ",tb_datos_medidor.__dict__)
  print("here is the accesorio ",ipt_accesorio_ids)
  print("here is the conexion alcantarillado ",tb_datos_conexion_alcantarillado.__dict__)
  print("here is the caja registro desague ",tb_datos_caja_registro_desague.__dict__)
  print("here is the caja alcantarillado ",tb_datos_tapa_caja_alcantarillado.__dict__)
  print("here is the sin conexion agua alc ",tb_datos_sin_conexion_agua_alc.__dict__)
  print("here is the datos complementarios ",tb_datos_complementarios.__dict__)
  print("here is the recoleccion basura ",tb_recoleccion_basura.__dict__)
  print("here is the ficha general",tb_ficha_tecnica.__dict__)
  print("here is the dict ",foreingObjectsIds)
  
  # tb_ficha_tecnica = getFichaTecnica(request)



def buscarCampos(request):
  if request.method == 'GET':
    context={
      'buscar_tipo': 1,
    }
    return render(request, 'buscar.html',context)
  else:
    filter_by = request.POST['filter']
    value_to_filter = request.POST['table_filter']
    
    if filter_by=="all":
      tbdatos = (
        TbNuevoCodigoCatastral.objects.select_related('fichatecnica','fichatecnica__datos_generales_usuario')
          .filter(fichatecnica__datos_generales_usuario_id__clave_catastral_actual__contains=value_to_filter) |
        TbNuevoCodigoCatastral.objects.select_related('responsableacometida')
          .filter(responsableacometida_id__cedula_identidad__contains=value_to_filter) |
        TbNuevoCodigoCatastral.objects.select_related('responsableacometida')
          .filter(responsableacometida_id__nombres_apellidos__contains=value_to_filter) 
        )
      
    if filter_by == "clave":
      tbdatos = ( 
        TbNuevoCodigoCatastral.objects.select_related('fichatecnica','fichatecnica__datos_generales_usuario')
          .filter(fichatecnica__datos_generales_usuario_id__clave_catastral_actual__contains=value_to_filter)
        )
    if filter_by == "ci":
      tbdatos = (
        TbNuevoCodigoCatastral.objects.select_related('responsableacometida')
          .filter(responsableacometida_id__cedula_identidad__contains=value_to_filter)
        )
    if filter_by == "name":
      tbdatos = (
        TbNuevoCodigoCatastral.objects.select_related('responsableacometida')
          .filter(responsableacometida_id__nombres_apellidos__contains=value_to_filter) 
        )
    context={
      'tbdatos': tbdatos,
      'buscar_tipo': 1,
    }
    return render(request, 'buscar.html', context)



def Data(conditions):
  tipo_usuarios= TbTipoUsuario.objects.all()
  predio_responsables= TbResponsablePredio.objects.all()
  tipo_predios = TbTipoPredio.objects.all()
  construccion_materiales = TbMaterialConstruccion.objects.all()
  servicio_tipos = TbTipoServicio.objects.all()
  predio_actividades = TbActividadPredio.objects.all()
  conexion_caracteristicas = TbCaracteristicasConexion.objects.all()
  conexion_diametros = TbDiametroConexion.objects.all()
  conexion_materiales = TbMaterialConexion.objects.all()
  conexion_situaciones = TbSituacionConexion.objects.all()
  caja_agua_ubicaciones = TbUbicacionCajagua.objects.all()
  caja_materiales = TbMaterialCaja.objects.all()
  caja_estados = TbEstadoCaja.objects.all()
  marco_tapa_materiales= TbMaterialMarcoTapa.objects.all()
  marco_tapa_estados= TbEstadoMArcoTapa.objects.all()
  medidor_diametros= TbDiametroMedidor.objects.all()
  accesorios= TbAccesorio.objects.all()
  alc_conexion_diametros= TbDiametroConexionAlc.objects.all()
  alc_conexion_materiales= TbMaterialConexionAlc.objects.all()
  alc_conexion_situaciones= TbSituacionConexionAlc.objects.all()
  caja_residual_ubicaciones= TbUbicacionCajaRD.objects.all()
  caja_residual_materiales= TbMaterialCajaRD.objects.all()
  caja_residual_estados= TbEstadoCajaRD.objects.all()
  tapa_materiales= TbMaterialTapa.objects.all()
  tapa_estados= TbEstadoTapa.objects.all()
  agua_potable_abastecimientos= TbAbastecimientoAguaPotable.objects.all()
  agua_potable_almacenamientos= TbAlmacenamientoAguaPotable.objects.all()
  saneamientos= TbSaneamiento.objects.all()
  jardin_huerto_tipos= TbJardinHuerto.objects.all()
  vereda_tipos= TbTipoVereda.objects.all()
  pavimentos= TbPavimento.objects.all()

  context={
    'header': conditions['header'],
    'has_edit_permission': conditions['has_edit_permission'],
    'edit_mode': conditions['edit_mode'],
    'mode': conditions['mode'],
    
    'tipo_usuarios': tipo_usuarios,
    'predio_responsables': predio_responsables,
    'tipo_predios': tipo_predios,
    'construccion_materiales': construccion_materiales,
    'servicio_tipos': servicio_tipos,
    'predio_actividades': predio_actividades,
    'conexion_caracteristicas': conexion_caracteristicas,
    'conexion_diametros': conexion_diametros,
    'conexion_materiales': conexion_materiales,
    'conexion_situaciones': conexion_situaciones,
    'caja_agua_ubicaciones': caja_agua_ubicaciones,
    'caja_materiales': caja_materiales,
    'caja_estados': caja_estados,
    'marco_tapa_materiales': marco_tapa_materiales,
    'marco_tapa_estados': marco_tapa_estados,
    'medidor_diametros': medidor_diametros,
    'accesorios': accesorios,
    'alc_conexion_diametros': alc_conexion_diametros,
    'alc_conexion_materiales': alc_conexion_materiales,
    'alc_conexion_situaciones': alc_conexion_situaciones,
    'caja_residual_ubicaciones': caja_residual_ubicaciones,
    'caja_residual_materiales': caja_residual_materiales,
    'caja_residual_estados': caja_residual_estados,
    'tapa_materiales': tapa_materiales,
    'tapa_estados': tapa_estados,
    'agua_potable_abastecimientos': agua_potable_abastecimientos,
    'agua_potable_almacenamientos': agua_potable_almacenamientos,
    'saneamientos': saneamientos,
    'jardin_huerto_tipos': jardin_huerto_tipos,
    'vereda_tipos': vereda_tipos,
    'pavimentos': pavimentos,
  }
  
  return context 


def saveDatosResponsableAcometida(request) -> TbDatosResponsableAcometida:
  DatosResponsableAcometida = TbDatosResponsableAcometida(
    cedula_identidad=request.POST['ipt_ci_ruc'],
    nombres_apellidos=request.POST['ipt_nombres_apellidos'],
  )
  DatosResponsableAcometida.save()
  return DatosResponsableAcometida

def getDatosResponsableAcometida(request) -> TbDatosResponsableAcometida:
  DatosResponsableAcometida = TbDatosResponsableAcometida(
    cedula_identidad=request.POST['ipt_ci_ruc'],
    nombres_apellidos=request.POST['ipt_nombres_apellidos'],
  )
  return DatosResponsableAcometida

def updateDatosResponsableAcometida(datosDatosResponsableAcometidaForm: TbDatosGeneralesUsuario, datosDatosResponsableAcometidaDB: TbDatosGeneralesUsuario) -> None:
  datosDatosResponsableAcometidaDB.cedula_identidad=datosDatosResponsableAcometidaForm.cedula_identidad
  datosDatosResponsableAcometidaDB.nombres_apellidos=datosDatosResponsableAcometidaForm.nombres_apellidos
  datosDatosResponsableAcometidaDB.save()
  return 

def saveDatosGenerales(request) -> TbDatosGeneralesUsuario:
  DatosGenerales = TbDatosGeneralesUsuario(
    direccion=request.POST['ipt_direccion'],
    numero_inscripcion=request.POST['ipt_num_inscripcion'],
    barrio=request.POST['ipt_lugar'],
    clave_catastral_actual=request.POST['ipt_codigo_actual'],
    esta_registrado=request.POST["rdo_esta_registrado"],
  )
  DatosGenerales.save()
  return DatosGenerales

def getDatosGenerales(request) -> TbDatosGeneralesUsuario:
  DatosGenerales = TbDatosGeneralesUsuario(
    direccion=request.POST['ipt_direccion'],
    numero_inscripcion=request.POST['ipt_num_inscripcion'],
    barrio=request.POST['ipt_lugar'],
    clave_catastral_actual=request.POST['ipt_codigo_actual'],
    esta_registrado=request.POST["rdo_esta_registrado"],
  )
  return DatosGenerales


def updateDatosGenerales(datosGeneralesForm: TbDatosGeneralesUsuario, datosGeneralesDB: TbDatosGeneralesUsuario) -> None:
  datosGeneralesDB.direccion=datosGeneralesForm.direccion
  datosGeneralesDB.numero_inscripcion=datosGeneralesForm.numero_inscripcion
  datosGeneralesDB.barrio=datosGeneralesForm.barrio
  datosGeneralesDB.clave_catastral_actual=datosGeneralesForm.clave_catastral_actual
  datosGeneralesDB.esta_registrado=datosGeneralesForm.esta_registrado
  datosGeneralesDB.save()
  return 


def saveNuevoCodigoCatastral(request, fore_data :dict) -> TbNuevoCodigoCatastral:
  nuevoCodigoCatastral = TbNuevoCodigoCatastral(
    provincia = request.POST['ipt_provincia'],
    canton = request.POST['ipt_canton'],
    parroquia = request.POST['ipt_parroquia'],
    zona = request.POST['ipt_zona'],
    sector = request.POST['ipt_sector'],
    manzana = request.POST['ipt_manzana'],
    predio = request.POST['ipt_predio'],
    conexion = request.POST['ipt_conexion'],
    fichatecnica=fore_data['tb_ficha_tecnica'],
    responsableacometida=fore_data['tb_datos_responsableacometida'],
    datos_conexion_agua_potable=fore_data['tb_datos_conexion_ap'],
    datos_marco_tapa_caja_agua=fore_data['tb_datos_marco_tapa_ca'],
    datos_caja_agua=fore_data['tb_caja_agua'],
    datos_medidor=fore_data['tb_datos_medidor'],
    estado_acometida_agua=2,
  )
  nuevoCodigoCatastral.save()
  return nuevoCodigoCatastral

def getNuevoCodigoCatastral(request) -> TbNuevoCodigoCatastral:
  nuevoCodigoCatastral = TbNuevoCodigoCatastral(
    provincia = request.POST['ipt_provincia'],
    canton = request.POST['ipt_canton'],
    parroquia = request.POST['ipt_parroquia'],
    zona = request.POST['ipt_zona'],
    sector = request.POST['ipt_sector'],
    manzana = request.POST['ipt_manzana'],
    predio = request.POST['ipt_predio'],
    conexion = request.POST['ipt_conexion']
  )
  return nuevoCodigoCatastral

def updateNuevoCodigoCatastral(datosNuevoCodigoCatastralForm: TbNuevoCodigoCatastral, datosNuevoCodigoCatastralDB: TbNuevoCodigoCatastral) -> None:
  datosNuevoCodigoCatastralDB.provincia = datosNuevoCodigoCatastralForm.provincia
  datosNuevoCodigoCatastralDB.canton = datosNuevoCodigoCatastralForm.canton
  datosNuevoCodigoCatastralDB.parroquia = datosNuevoCodigoCatastralForm.parroquia
  datosNuevoCodigoCatastralDB.zona = datosNuevoCodigoCatastralForm.zona
  datosNuevoCodigoCatastralDB.sector = datosNuevoCodigoCatastralForm.sector
  datosNuevoCodigoCatastralDB.manzana = datosNuevoCodigoCatastralForm.manzana
  datosNuevoCodigoCatastralDB.predio = datosNuevoCodigoCatastralForm.predio
  datosNuevoCodigoCatastralDB.conexion = datosNuevoCodigoCatastralForm.conexion
  datosNuevoCodigoCatastralDB.save()
  return


def getDatosInmueble(request) -> TbDatosInmueble:
  nuevoDatosInmueble = TbDatosInmueble(
    numero_pisos = request.POST['ipt_numero_pisos'], 
    unidades_domestico = request.POST['ipt_uu_domestico'],
    unidades_publico = request.POST['ipt_uu_publico'],
    unidades_comercial = request.POST['ipt_uu_comercial'], 
    unidades_industrial = request.POST['ipt_uu_industrial'],
    habitada = request.POST['rdo_habitada'],
    numero_personas = request.POST['ipt_numero_personas'],
    numero_familias = request.POST['ipt_numero_familias'], 
    pozo_artesiano = request.POST['rdo_pozo_artesiano'],
    tiene_piscina = request.POST['rdo_piscina'],
    actividad_predio_id = request.POST['slc_actividad_predio'],
    tipo_predio_id = request.POST['slc_tipo_predio'],
    material_construccion_id = request.POST['slc_material_construccion'],
    tipo_servicio_id = request.POST['slc_tipo_servicio']
  )
  return nuevoDatosInmueble


def updateDatosInmueble(datosInmuebleForm: TbDatosInmueble, datosInmuebleDB: TbDatosInmueble) -> None:
  if (datosInmuebleForm.numero_pisos) : datosInmuebleDB.numero_pisos = datosInmuebleForm.numero_pisos
  if (datosInmuebleForm.unidades_domestico) : datosInmuebleDB.unidades_domestico =datosInmuebleForm.unidades_domestico
  if (datosInmuebleForm.unidades_publico) : datosInmuebleDB.unidades_publico = datosInmuebleForm.unidades_publico
  if (datosInmuebleForm.unidades_comercial) : datosInmuebleDB.unidades_comercial = datosInmuebleForm.unidades_comercial
  if (datosInmuebleForm.unidades_industrial) : datosInmuebleDB.unidades_industrial = datosInmuebleForm.unidades_industrial
  if (datosInmuebleForm.numero_personas) : datosInmuebleDB.numero_personas = datosInmuebleForm.numero_personas
  if (datosInmuebleForm.numero_familias) : datosInmuebleDB.numero_familias = datosInmuebleForm.numero_familias
  datosInmuebleDB.habitada = datosInmuebleForm.habitada
  datosInmuebleDB.pozo_artesiano = datosInmuebleForm.pozo_artesiano
  datosInmuebleDB.tiene_piscina = datosInmuebleForm.tiene_piscina
  datosInmuebleDB.actividad_predio_id = datosInmuebleForm.actividad_predio_id
  datosInmuebleDB.tipo_predio_id = datosInmuebleForm.tipo_predio_id
  datosInmuebleDB.material_construccion_id = datosInmuebleForm.material_construccion_id
  datosInmuebleDB.tipo_servicio_id = datosInmuebleForm.tipo_servicio_id
  datosInmuebleDB.save()
  return

def saveDatosConexionAP(request) -> TbDatosConexionAguaPotable:
  nuevoDatosConexionAP = TbDatosConexionAguaPotable(
    fecha_instalacion = request.POST['ipt_fecha_instalacion'] if request.POST['ipt_fecha_instalacion'] else None,
    caracteristicas_conexion_id = request.POST['slc_caracteristica_conexion_ap'],
    diametro_conexion_id = request.POST['slc_diametro_conexion_ap'],
    material_conexion_id = request.POST['slc_material_conexion_ap'],
    situacion_conexion_id = request.POST['slc_situacion_conexion_ap']
  )
  nuevoDatosConexionAP.save()
  return nuevoDatosConexionAP

def getDatosConexionAP(request) -> TbDatosConexionAguaPotable:
  nuevoDatosConexionAP = TbDatosConexionAguaPotable(
    fecha_instalacion = request.POST['ipt_fecha_instalacion'],
    caracteristicas_conexion_id = request.POST['slc_caracteristica_conexion_ap'],
    diametro_conexion_id = request.POST['slc_diametro_conexion_ap'],
    material_conexion_id = request.POST['slc_material_conexion_ap'],
    situacion_conexion_id = request.POST['slc_situacion_conexion_ap']
  )
  return nuevoDatosConexionAP

def updateDatosConexionAP(datosConexionAguaPotableForm: TbDatosConexionAguaPotable, datosConexionAguaPotableDB: TbDatosConexionAguaPotable) -> None:
  if (datosConexionAguaPotableForm.fecha_instalacion) : datosConexionAguaPotableDB.fecha_instalacion = datosConexionAguaPotableForm.fecha_instalacion 
  datosConexionAguaPotableDB.caracteristicas_conexion_id = datosConexionAguaPotableForm.caracteristicas_conexion_id 
  datosConexionAguaPotableDB.diametro_conexion_id = datosConexionAguaPotableForm.diametro_conexion_id 
  datosConexionAguaPotableDB.material_conexion_id = datosConexionAguaPotableForm.material_conexion_id 
  datosConexionAguaPotableDB.situacion_conexion_id = datosConexionAguaPotableForm.situacion_conexion_id 
  datosConexionAguaPotableDB.save() 
  return

def saveDatosCajaAgua(request) -> TbDatosCajaAgua:
  nuevoDatosConexionAP = TbDatosCajaAgua(
    ubicacion_caja_agua_id = request.POST['slc_ubicacion_caja'],
    material_caja_id = request.POST['slc_material_caja'],
    estado_caja_id = request.POST['slc_estado_caja']
  )
  nuevoDatosConexionAP.save()
  return nuevoDatosConexionAP

def saveDatosCajaAguaAcometida(request) -> TbDatosCajaAgua:
  nuevoDatosConexionAP = TbDatosCajaAgua(
    ubicacion_caja_agua_id = None,
    material_caja_id = None,
    estado_caja_id = None,
  )
  nuevoDatosConexionAP.save()
  return nuevoDatosConexionAP

def getDatosCajaAgua(request) -> TbDatosCajaAgua:
  nuevoDatosConexionAP = TbDatosCajaAgua(
    ubicacion_caja_agua_id = request.POST['slc_ubicacion_caja'],
    material_caja_id = request.POST['slc_material_caja'],
    estado_caja_id = request.POST['slc_estado_caja']
  )
  return nuevoDatosConexionAP

def updateDatosCajaAgua(datosCajaAguaForm: TbDatosCajaAgua, datosCajaAguaDB: TbDatosCajaAgua) -> None:
  datosCajaAguaDB.ubicacion_caja_agua_id = datosCajaAguaForm.ubicacion_caja_agua_id
  datosCajaAguaDB.material_caja_id = datosCajaAguaForm.material_caja_id
  datosCajaAguaDB.estado_caja_id = datosCajaAguaForm.estado_caja_id
  datosCajaAguaDB.save()

def saveDatosMarcoTapaCA(request) -> TbDatosMarcoTapaCajaAgua:
  nuevoDatosMarcoTapaCA = TbDatosMarcoTapaCajaAgua(
    material_marco_tapa_id =  request.POST['slc_material_marco_tapa'],
    estado_marco_tapa_id =  request.POST['slc_estado_marco_tapa'],
  )
  nuevoDatosMarcoTapaCA.save()
  return nuevoDatosMarcoTapaCA

def getDatosMarcoTapaCA(request) -> TbDatosMarcoTapaCajaAgua:
  nuevoDatosMarcoTapaCA = TbDatosMarcoTapaCajaAgua(
    material_marco_tapa_id =  request.POST['slc_material_marco_tapa'],
    estado_marco_tapa_id =  request.POST['slc_estado_marco_tapa'],
  )
  return nuevoDatosMarcoTapaCA

def updateDatosMarcoTapaCA(datosCajaAguaForm: TbDatosMarcoTapaCajaAgua, datosCajaAguaDB: TbDatosMarcoTapaCajaAgua):
  datosCajaAguaDB.material_marco_tapa_id = datosCajaAguaForm.material_marco_tapa_id 
  datosCajaAguaDB.estado_marco_tapa_id = datosCajaAguaForm.estado_marco_tapa_id 
  datosCajaAguaDB.save()
  return

def saveDatosMedidor(request) -> TbDatosMedidor:
  nuevoDatosMedidor = TbDatosMedidor(
    numero_medidor = request.POST['ipt_numero_medidor'],
    lectura = request.POST['ipt_lectura'],
    marca_medidor = request.POST['ipt_marca_medidor'],
    no_determinado = request.POST.get('cek_nodeterminado', False),
    operativo = request.POST.get('ipt_datos_medidor_operativo', False),
    luna_opaca = request.POST.get('ipt_datos_medidor_luna_opaca', False),
    luna_rota = request.POST.get('ipt_datos_medidor_luna_rota', False),
    sin_tapa = request.POST.get('ipt_datos_medidor_sin_tapa', False),
    malogrado = request.POST.get('ipt_datos_medidor_malogrado', False),
    diametro_medidor_id = request.POST['slc_diametro_medidor']
  )
  nuevoDatosMedidor.save()
  return nuevoDatosMedidor

def getDatosMedidor(request) -> TbDatosMedidor:
  nuevoDatosMedidor = TbDatosMedidor(
    numero_medidor = request.POST['ipt_numero_medidor'],
    lectura = request.POST['ipt_lectura'],
    marca_medidor = request.POST['ipt_marca_medidor'],
    no_determinado = request.POST.get('cek_nodeterminado', False),
    operativo = request.POST.get('ipt_datos_medidor_operativo', False),
    luna_opaca = request.POST.get('ipt_datos_medidor_luna_opaca', False),
    luna_rota = request.POST.get('ipt_datos_medidor_luna_rota', False),
    sin_tapa = request.POST.get('ipt_datos_medidor_sin_tapa', False),
    malogrado = request.POST.get('ipt_datos_medidor_malogrado', False),
    diametro_medidor_id = request.POST['slc_diametro_medidor']
  )
  return nuevoDatosMedidor

def updateDatosMedidor(datosMedidorForm: TbDatosMedidor, datosMedidorDB: TbDatosMedidor) -> None:
  if (datosMedidorForm.numero_medidor) : datosMedidorDB.numero_medidor = datosMedidorForm.numero_medidor 
  datosMedidorDB.lectura = datosMedidorForm.lectura 
  datosMedidorDB.marca_medidor = datosMedidorForm.marca_medidor 
  datosMedidorDB.no_determinado = datosMedidorForm.no_determinado 
  datosMedidorDB.operativo = datosMedidorForm.operativo 
  datosMedidorDB.luna_opaca = datosMedidorForm.luna_opaca 
  datosMedidorDB.luna_rota = datosMedidorForm.luna_rota 
  datosMedidorDB.sin_tapa = datosMedidorForm.sin_tapa 
  datosMedidorDB.malogrado = datosMedidorForm.malogrado 
  datosMedidorDB.diametro_medidor_id = datosMedidorForm.diametro_medidor_id 
  datosMedidorDB.save()
  return

def saveDatosMedidorAccesorio(request, medidor_id: int) -> None:
  ipt_accesorio_ids = request.POST.getlist('ipt_accesorio_id')
  estado_accesorios = request.POST.getlist('slc_estado_accesorio')
  for ipt_accesorio_id,estado_accesorio in zip(ipt_accesorio_ids, estado_accesorios):
    getDatosMedidorAccesorio= TbMedidorAccesorio.objects.get(datos_medidor_id = medidor_id, accesorio_id=ipt_accesorio_id)
    getDatosMedidorAccesorio.estado_accesorio = estado_accesorio
    getDatosMedidorAccesorio.save()
  return

def getDatosMedidorAccesorio(request):
  ipt_accesorio_ids = request.POST.getlist('ipt_accesorio_id')
  estado_accesorios = request.POST.getlist('slc_estado_accesorio')
  return ipt_accesorio_ids, estado_accesorios

def updateDatosMedidorAccesorio(ipt_accesorio_ids: list, estado_accesorios: list, medidor_id: int) -> None:
  for ipt_accesorio_id,estado_accesorio in zip(ipt_accesorio_ids, estado_accesorios):
    getDatosMedidorAccesorio= TbMedidorAccesorio.objects.get(datos_medidor_id = medidor_id, accesorio_id=ipt_accesorio_id)
    getDatosMedidorAccesorio.estado_accesorio = estado_accesorio
    getDatosMedidorAccesorio.save()
  return

def getDatosConexionAlcantarillado(request):
  nuevoDatosConexionAlcantarillado = TbDatosConexionAlcantarillado(
    sin_caja_conexion_directa = request.POST.get('ipt_sin_caja_conexion_directa', False),
    con_caja_sin_medidor = request.POST.get('ipt_con_caja_sin_medidor', False),
    con_caja_con_medidor = request.POST.get('ipt_con_caja_con_medidor', False),
    sin_conexion = request.POST.get('ipt_sin_conexion_alc', False),
    fecha_instalacion = request.POST['ipt_fecha_instalacion_alc'],
    diametro_conexion_id = request.POST['slc_diametro_conexion_alc'],
    material_conexion_id = request.POST['slc_material_conexion_alc'],
    situacion_conexion_id = request.POST['slc_situacion_conexion_alc']
  )
  return nuevoDatosConexionAlcantarillado

def updateDatosConexionAlcantarillado(datosConexionAlcantarilladoForm: TbDatosConexionAlcantarillado, datosConexionAlcantarilladoDB: TbDatosConexionAlcantarillado):
  datosConexionAlcantarilladoDB.sin_caja_conexion_directa = datosConexionAlcantarilladoForm.sin_caja_conexion_directa
  datosConexionAlcantarilladoDB.con_caja_sin_medidor = datosConexionAlcantarilladoForm.con_caja_sin_medidor
  datosConexionAlcantarilladoDB.con_caja_con_medidor = datosConexionAlcantarilladoForm.con_caja_con_medidor
  datosConexionAlcantarilladoDB.sin_conexion = datosConexionAlcantarilladoForm.sin_conexion
  datosConexionAlcantarilladoDB.fecha_instalacion = datosConexionAlcantarilladoForm.fecha_instalacion
  datosConexionAlcantarilladoDB.diametro_conexion_id = datosConexionAlcantarilladoForm.diametro_conexion_id
  datosConexionAlcantarilladoDB.material_conexion_id = datosConexionAlcantarilladoForm.material_conexion_id
  datosConexionAlcantarilladoDB.situacion_conexion_id = datosConexionAlcantarilladoForm.situacion_conexion_id
  datosConexionAlcantarilladoDB.save()
  return

def getDatosCajaRegistroDesague(request):
  nuevoDatosCajaRegistroDesague = TbDatosCajaRegistroDesague(
    ubicacion_caja_id = request.POST['slc_ubicacion_caja_rd'],
    material_caja_id = request.POST['slc_material_caja_rd'],
    estado_caja_id = request.POST['slc_estado_caja_rd'],
    tiene_descargas_aass_aall = request.POST['rdo_descargas_asss_all']
  )
  return nuevoDatosCajaRegistroDesague

def updateDatosCajaRegistroDesague(datosCajaRegistroDesagueForm: TbDatosCajaRegistroDesague, datosCajaRegistroDesagueDB: TbDatosCajaRegistroDesague):
  datosCajaRegistroDesagueDB.ubicacion_caja_id = datosCajaRegistroDesagueForm.ubicacion_caja_id
  datosCajaRegistroDesagueDB.material_caja_id = datosCajaRegistroDesagueForm.material_caja_id
  datosCajaRegistroDesagueDB.estado_caja_id = datosCajaRegistroDesagueForm.estado_caja_id
  datosCajaRegistroDesagueDB.tiene_descargas_aass_aall = datosCajaRegistroDesagueForm.tiene_descargas_aass_aall
  return datosCajaRegistroDesagueDB

def getDatosTapaCajaAlcantarillado(request):
  nuevoDatosTapaCajaAlcantarillado = TbDatosTapaCajaAlcantarillado(
    material_tapa_id = request.POST['slc_material_tapa'],
    estado_tapa_id = request.POST['slc_estado_tapa']
  )
  return nuevoDatosTapaCajaAlcantarillado

def updateDatosTapaCajaAlcantarillado(datosTapaCajaAlcantarilladoForm: TbDatosTapaCajaAlcantarillado, datosTapaCajaAlcantarilladoDB: TbDatosTapaCajaAlcantarillado):
  datosTapaCajaAlcantarilladoDB.material_tapa_id = datosTapaCajaAlcantarilladoForm.material_tapa_id
  datosTapaCajaAlcantarilladoDB.estado_tapa_id = datosTapaCajaAlcantarilladoForm.estado_tapa_id
  return datosTapaCajaAlcantarilladoDB

def getDatosSinConexionAguaAlcantarillado(request):
  nuevoDatosSinConexionAguaAlcantarillado = TbDatosSinConexionAguaAlcantarillado(
    abastecimiento_agua_id = request.POST['slc_abastecimiento_agua'],
    almacenamiento_agua_id = request.POST['slc_almacenamiento_agua'],
    numero_horas_abastecimiento = request.POST['ipt_horas_abastecimi'],
    saneamiento_id = request.POST['slc_saneamiento']
  ) 
  return nuevoDatosSinConexionAguaAlcantarillado

def updateDatosSinConexionAguaAlcantarillado(datosSinConexionAguaAlcantarilladoForm: TbDatosSinConexionAguaAlcantarillado, datosSinConexionAguaAlcantarilladoDB: TbDatosSinConexionAguaAlcantarillado):
  datosSinConexionAguaAlcantarilladoDB.abastecimiento_agua_id = datosSinConexionAguaAlcantarilladoForm.abastecimiento_agua_id
  datosSinConexionAguaAlcantarilladoDB.almacenamiento_agua_id = datosSinConexionAguaAlcantarilladoForm.almacenamiento_agua_id
  datosSinConexionAguaAlcantarilladoDB.numero_horas_abastecimiento = datosSinConexionAguaAlcantarilladoForm.numero_horas_abastecimiento
  datosSinConexionAguaAlcantarilladoDB.saneamiento_id = datosSinConexionAguaAlcantarilladoForm.saneamiento_id
  return datosSinConexionAguaAlcantarilladoDB

def saveDatosComplementarios(request) -> TbDatosComplementarios:
  nuevoDatosComplementarios = TbDatosComplementarios(
    jardin_huerto_id = request.POST['slc_jardin_huerto'],
    pavimento_id = request.POST['slc_pavimento'],
    tipo_vereda_id = request.POST['slc_tipo_vereda']
  )
  nuevoDatosComplementarios.save()
  return nuevoDatosComplementarios

def getDatosComplementarios(request) -> TbDatosComplementarios:
  nuevoDatosComplementarios = TbDatosComplementarios(
    jardin_huerto_id = request.POST['slc_jardin_huerto'],
    pavimento_id = request.POST['slc_pavimento'],
    tipo_vereda_id = request.POST['slc_tipo_vereda']
  )
  return nuevoDatosComplementarios

def updateDatosComplementarios(datosComplementariosForm: TbDatosComplementarios, datosComplementariosDB: TbDatosComplementarios) -> None:
  datosComplementariosDB.jardin_huerto_id = datosComplementariosForm.jardin_huerto_id
  datosComplementariosDB.pavimento_id = datosComplementariosForm.pavimento_id
  datosComplementariosDB.tipo_vereda_id = datosComplementariosForm.tipo_vereda_id
  datosComplementariosDB.save()
  return

def getRecoleccionBasura(request) -> TbRecoleccionBasura:
  nuevoRecoleccionBasura = TbRecoleccionBasura(
    tiene_recoleccion_basura_predio = request.POST['rdo_tiene_recoleccion'],
    clasifica_residuos_domesticos = request.POST['rdo_clasifica_residuos'],
    tiene_contenedores_cercanos_predio = request.POST['rdo_contenedores_cercanos'],
    especifique_numero_cuadras = request.POST['ipt_numero_cuadras']
  )
  return nuevoRecoleccionBasura

def updateRecoleccionBasura(datosRecoleccionBasuraForm: TbRecoleccionBasura, datosRecoleccionBasuraDB: TbRecoleccionBasura) -> None:
  datosRecoleccionBasuraDB.tiene_recoleccion_basura_predio = datosRecoleccionBasuraForm.tiene_recoleccion_basura_predio
  datosRecoleccionBasuraDB.clasifica_residuos_domesticos = datosRecoleccionBasuraForm.clasifica_residuos_domesticos
  datosRecoleccionBasuraDB.tiene_contenedores_cercanos_predio = datosRecoleccionBasuraForm.tiene_contenedores_cercanos_predio
  if (datosRecoleccionBasuraForm.especifique_numero_cuadras) : datosRecoleccionBasuraDB.especifique_numero_cuadras = datosRecoleccionBasuraForm.especifique_numero_cuadras
  print(datosRecoleccionBasuraDB.__dict__)
  print(datosRecoleccionBasuraForm.__dict__)
  datosRecoleccionBasuraDB.save()
  return

def getFichaTecnica(request, isCoordAgua: bool, isCoordAlc: bool, isCoordDesechos: bool) -> TbFichaTecnica:
  if(isCoordAgua):  
    nuevoFichaTecnica = TbFichaTecnica(
      tipo_usuario_id = request.POST['slc_tipo_usuario'],
      responsable_predio_id = request.POST['rdo_responsable_predio'],
    )
    return nuevoFichaTecnica

  if(isCoordDesechos):  
    nuevoFichaTecnica = TbFichaTecnica(
      tipo_usuario_id = request.POST['slc_tipo_usuario'],
    )
    return nuevoFichaTecnica
  nuevoFichaTecnica = TbFichaTecnica(
    numero_ficha = request.POST['ipt_numero_ficha'],
    tipo_usuario_id = request.POST['slc_tipo_usuario'],
    responsable_predio_id = request.POST['rdo_responsable_predio'],
    observaciones = request.POST['txa_observaciones'],
    tercera_edad = request.POST['rdo_tercera_edad'],
    tiene_carne_conadis = request.POST['rdo_carne_conadis'],
    fecha_encuesta = request.POST['ipt_fecha_encuesta'],
  )
  return nuevoFichaTecnica

def updateFichaTecnica(datosFichaTecnicaForm: TbFichaTecnica, datosFichaTecnicaDB: TbFichaTecnica) -> None:
  if (datosFichaTecnicaForm.numero_ficha): datosFichaTecnicaDB.numero_ficha = datosFichaTecnicaForm.numero_ficha
  if (datosFichaTecnicaForm.tipo_usuario_id): datosFichaTecnicaDB.tipo_usuario_id = datosFichaTecnicaForm.tipo_usuario_id
  if (datosFichaTecnicaForm.responsable_predio_id): datosFichaTecnicaDB.responsable_predio_id = datosFichaTecnicaForm.responsable_predio_id
  if (datosFichaTecnicaForm.observaciones): datosFichaTecnicaDB.observaciones = datosFichaTecnicaForm.observaciones
  if (datosFichaTecnicaForm.tercera_edad): datosFichaTecnicaDB.tercera_edad = datosFichaTecnicaForm.tercera_edad
  if (datosFichaTecnicaForm.tiene_carne_conadis): datosFichaTecnicaDB.tiene_carne_conadis = datosFichaTecnicaForm.tiene_carne_conadis
  if (datosFichaTecnicaForm.fecha_encuesta): datosFichaTecnicaDB.fecha_encuesta = datosFichaTecnicaForm.fecha_encuesta
  datosFichaTecnicaDB.save()
  return
