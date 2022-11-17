from django import forms 
from django.forms import ValidationError
from crispy_forms.helper import FormHelper 
from .models import TbDatosGeneralesUsuario, TbNuevoCodigoCatastral, TbFichaTecnica, TbDatosInmueble, TbDatosConexionAguaPotable, TbDatosCajaAgua, TbDatosMarcoTapaCajaAgua, TbDatosMedidor, TbDatosConexionAlcantarillado, TbDatosCajaRegistroDesague, TbDatosTapaCajaAlcantarillado, TbDatosSinConexionAguaAlcantarillado, TbDatosComplementarios, TbRecoleccionBasura

class TbDatosGeneralesUsuarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TbDatosGeneralesUsuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    
    def clean_direccion(self):
        direccion = self.cleaned_data["direccion"]
        if direccion == 'hola':
            raise ValidationError("No se puede ingresar hola")

        return direccion 
    
    class Meta: 
        model = TbDatosGeneralesUsuario
        fields = ['direccion', 'numero_inscripcion', 'barrio', 'clave_catastral_actual', 'esta_registrado']

        widgets = {
            'cedula_identidad': forms.TextInput(
                attrs = {
                    'class':'border-success',
                    'placeholder':'Ingrese el CI/RUC',
                    'maxlength':'13'
                }
            ),
            'nombres_apellidos': forms.TextInput(
                attrs = {
                    'class':'border-success',
                    'placeholder':'Ingrese los nombres y apellidos',
                    'maxlength':'180'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class':' border-success',
                    'placeholder':'Ingrese la dirección'
                }
            ),
            'numero_inscripcion': forms.TextInput(
                attrs = {
                    'class':'border-success',
                    'placeholder':'Ingrese el número de inscripción',
                    'maxlength':'4'
                }
            ),
            'barrio': forms.TextInput(
                attrs = {
                    'class':'border-success',
                    'placeholder': 'Ingrese el lugar'
                }
            ),
            'clave_catastral_actual': forms.TextInput(
                attrs = {
                    'class':'border-success',
                    'placeholder':'Ingrese el código catastral actual',
                    'maxlength':'15'
                }
            ),
            'esta_registrado': forms.NullBooleanSelect(
                attrs={
                    'class':'border-success'
                }
            )
        }

class TbNuevoCodigoCatastralForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbNuevoCodigoCatastralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbNuevoCodigoCatastral
        fields = ['provincia', 'canton', 'parroquia', 'zona', 'sector', 'manzana', 'predio', 'conexion']

        widgets = {
            'provincia': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'canton': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'parroquia': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'zona': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'sector': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'manzana': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'predio': forms.NumberInput(attrs = {'class':'border-success', 'maxlength':'2'}),
            'conexion': forms.TextInput(attrs = {'class':'border-success', 'maxlength':'2'})
        }

class TbFichaTecnicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbFichaTecnicaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbFichaTecnica
        fields = ['numero_ficha', 'tipo_usuario', 'responsable_predio', 'observaciones', 'tercera_edad', 'tiene_carne_conadis', 'fecha_encuesta']

        widgets = {
            'numero_ficha': forms.TextInput(
                attrs = {
                    'class':'form-control border-success',
                    'required':'required',
                    'maxlength':'9',
                    'placeholder':'Escriba el número de ficha'
                }
            ),
            'responsable_predio': forms.Select(attrs={'class':'border-success'}),
            'tipo_usuario': forms.Select(attrs={'class':'border-success'}),
            'observaciones': forms.Textarea(attrs = {'class':'border-success','placeholder':'Ingrese las observaciones'}),
            'tercera_edad': forms.NullBooleanSelect(attrs = {'class':'border-success'}),
            'tiene_carne_conadis': forms.NullBooleanSelect(attrs = {'class':'border-success'}),
            'fecha_encuesta': forms.DateInput(attrs = {'class':'border-success', 'type':'date'}),

        }

class TbDatosInmuebleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosInmuebleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosInmueble
        fields = ['numero_pisos', 'unidades_domestico', 'unidades_publico', 'unidades_comercial', 'unidades_industrial', 'habitada', 'numero_personas',
                  'numero_familias', 'pozo_artesiano', 'tiene_piscina', 'actividad_predio', 'tipo_predio', 'material_construccion', 'tipo_servicio']

        widgets = {
            'numero_pisos': forms.NumberInput(attrs = {'class':'border-success'}),
            'unidades_domestico': forms.NumberInput(attrs = {'class':'border-success'}),
            'unidades_publico': forms.NumberInput(attrs = {'class':'border-success'}),
            'unidades_comercial': forms.NumberInput(attrs = {'class':'border-success'}),
            'unidades_industrial': forms.NumberInput(attrs = {'class':'border-success'}),
            'habitada' : forms.NullBooleanSelect(attrs={'class':'border-success'}),
            'numero_personas' : forms.NumberInput(attrs = {'class':'border-success'}),
            'numero_familias' : forms.NumberInput(attrs = {'class':'border-success'}),
            'pozo_artesiano' : forms.CheckboxInput(attrs={'class':'border-success'}),
            'tiene_piscina' : forms.CheckboxInput(attrs={'class':'border-success'}),
            'actividad_predio': forms.Select(attrs = {'class':'border-success'}),
            'tipo_predio': forms.Select(attrs = {'class':'border-success'}),
            'material_construccion': forms.Select(attrs = {'class':'border-success'}),
            'tipo_servicio': forms.Select(attrs = {'class':'border-success'}),            
        }

class TbDatosConexionAguaPotableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosConexionAguaPotableForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosConexionAguaPotable
        fields = ['fecha_instalacion', 'caracteristicas_conexion', 'diametro_conexion', 'material_conexion', 'situacion_conexion']

        widgets = {
            'fecha_instalacion': forms.DateInput(attrs = {'class':'border-success', 'type':'date'}),
            'caracteristicas_conexion': forms.Select(attrs = {'class':'border-success'}),
            'diametro_conexion': forms.Select(attrs = {'class':'border-success'}),
            'material_conexion': forms.Select(attrs = {'class':'border-success'}),
            'situacion_conexion': forms.Select(attrs = {'class':'border-success'})    
        }

class TbDatosCajaAguaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosCajaAguaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosCajaAgua
        fields = ['ubicacion_caja_agua', 'material_caja', 'estado_caja']

        widgets = {
            'ubicacion_caja_agua': forms.Select(attrs = {'class':'border-success'}),
            'material_caja': forms.Select(attrs = {'class':'border-success'}),
            'estado_caja': forms.Select(attrs = {'class':'border-success'}), 
        }

class TbDatosMarcoTapaCajaAguaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosMarcoTapaCajaAguaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosMarcoTapaCajaAgua
        fields = ['material_marco_tapa', 'estado_marco_tapa']

        widgets = {
            'material_marco_tapa': forms.Select(attrs = {'class':'border-success'}),
            'estado_marco_tapa': forms.Select(attrs = {'class':'border-success'})
        }

class TbDatosMedidorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosMedidorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosMedidor
        fields = ['numero_medidor', 'lectura', 'marca_medidor', 'no_determinado', 'operativo', 'luna_opaca', 'luna_rota', 'sin_tapa', 
                  'malogrado', 'estado_niple_estandar', 'estado_llave_paso', 'estado_directo', 'estado_codo', 'estado_tubo_salida', 
                  'estado_tubo_entrada', 'diametro_medidor']

        widgets = {
            'numero_medidor': forms.NumberInput(attrs = {'class':'border-success'}),
            'lectura': forms.NumberInput(attrs = {'class':'border-success'}),
            'marca_medidor': forms.TextInput(attrs = {'class':'border-success'}),
            'no_determinado': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'operativo': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'luna_opaca' : forms.CheckboxInput(attrs={'class':'border-success'}),
            'luna_rota' : forms.CheckboxInput(attrs = {'class':'border-success'}),
            'sin_tapa' : forms.CheckboxInput(attrs = {'class':'border-success'}),
            'malogrado' : forms.CheckboxInput(attrs={'class':'border-success'}),
            'estado_niple_estandar' : forms.Select(attrs={'class':'border-success'}),
            'estado_llave_paso': forms.Select(attrs = {'class':'border-success'}),
            'estado_directo': forms.Select(attrs = {'class':'border-success'}),
            'estado_codo': forms.Select(attrs = {'class':'border-success'}),
            'estado_tubo_salida': forms.Select(attrs = {'class':'border-success'}),            
            'estado_tubo_entrada': forms.Select(attrs = {'class':'border-success'}),            
            'diametro_medidor': forms.Select(attrs = {'class':'border-success'}),            
        }

class TbDatosConexionAlcantarilladoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosConexionAlcantarilladoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosConexionAlcantarillado
        fields = ['sin_caja_conexion_directa', 'con_caja_sin_medidor', 'con_caja_con_medidor', 'sin_conexion', 'fecha_instalacion', 
                  'diametro_conexion', 'material_conexion', 'situacion_conexion']

        widgets = {
            'sin_caja_conexion_directa': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'con_caja_sin_medidor': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'con_caja_con_medidor': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'sin_conexion': forms.CheckboxInput(attrs = {'class':'border-success'}),
            'fecha_instalacion': forms.DateInput(attrs = {'class':'border-success', 'type':'date'}),
            'diametro_conexion' : forms.Select(attrs={'class':'border-success'}),
            'material_conexion' : forms.Select(attrs = {'class':'border-success'}),
            'situacion_conexion' : forms.Select(attrs = {'class':'border-success'}),          
        }

class TbDatosCajaRegistroDesagueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosCajaRegistroDesagueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosCajaRegistroDesague
        fields = ['ubicacion_caja', 'material_caja', 'estado_caja', 'tiene_descargas_aass_aall']

        widgets = {
            'ubicacion_caja': forms.Select(attrs = {'class':'border-success'}),
            'material_caja': forms.Select(attrs = {'class':'border-success'}),
            'estado_caja': forms.Select(attrs = {'class':'border-success'}),
            'tiene_descargas_aass_aall': forms.NullBooleanSelect(attrs = {'class':'border-success'}),  
        }

class TbDatosTapaCajaAlcantarilladoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosTapaCajaAlcantarilladoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        
    class Meta:
        model = TbDatosTapaCajaAlcantarillado
        fields = ['material_tapa', 'estado_tapa']

        widgets = {
            'material_tapa': forms.Select(attrs = {'class':'border-success'}),
            'estado_tapa': forms.Select(attrs = {'class':'border-success'}),
        }

class TbDatosSinConexionAguaAlcantarilladoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosSinConexionAguaAlcantarilladoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosSinConexionAguaAlcantarillado
        fields = ['abastecimiento_agua', 'almacenamiento_agua', 'numero_horas_abastecimiento', 'saneamiento']

        widgets = {
            'abastecimiento_agua': forms.Select(attrs = {'class':'border-success'}),
            'almacenamiento_agua': forms.Select(attrs = {'class':'border-success'}),
            'numero_horas_abastecimiento': forms.NumberInput(attrs = {'class':'border-success'}),
            'saneamiento': forms.Select(attrs = {'class':'border-success'}),
        }

class TbDatosComplementariosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbDatosComplementariosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbDatosComplementarios
        fields = ['jardin_huerto', 'pavimento', 'tipo_vereda']

        widgets = {
            'jardin_huerto': forms.Select(attrs = {'class':'border-success'}),
            'pavimento': forms.Select(attrs = {'class':'border-success'}),
            'tipo_vereda': forms.Select(attrs = {'class':'border-success'}),
        }

class TbRecoleccionBasuraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TbRecoleccionBasuraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = TbRecoleccionBasura
        fields = ['tiene_recoleccion_basura_predio', 'clasifica_residuos_domesticos', 'tiene_contenedores_cercanos_predio', 'especifique_numero_cuadras']

        widgets = {
            'tiene_recoleccion_basura_predio': forms.NullBooleanSelect(attrs = {'class':'border-success'}),
            'clasifica_residuos_domesticos': forms.NullBooleanSelect(attrs = {'class':'border-success'}),
            'tiene_contenedores_cercanos_predio': forms.NullBooleanSelect(attrs = {'class':'border-success'}),
            'especifique_numero_cuadras': forms.NumberInput(attrs = {'class':'border-success'}),
        }