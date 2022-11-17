// document.getElementById("cancelEdit")
//     .addEventListener("click", () => {
//         if (confirm("Seguro deseas cancelar?")) {
//             document.getElementById("edit_content").hidden = false;
//             document.getElementById("exit_edit_content").hidden = true;
//             var text_inputs =  document.getElementsByClassName("form-control");
// 			var text_inputs2 =  document.getElementsByClassName("validacion_input");
//             var radio_buttons =  document.getElementsByClassName("form-check-input");
//             var form_selects =  document.getElementsByClassName("form-select");
//             disableElements(text_inputs);
// 			disableElements(text_inputs2);
//             disableElements(radio_buttons);
//             disableElements(form_selects);
//         }
// }, false);
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/, // 7 a 14 numeros.
	direcciones: /^[a-zA-ZÀ-ÿ\s0-9\-\_]{1,255}$/, // Cualquier tipo de caracter 
	soloNumeros: /^[0-9]+$/, 
	validacionNumeroFicha: /^[0-9]{9}$/, 
	validacionCodigoCatastral: /^[0-9]{15}$/, 
	validacionCodigoActual: /^[0-9]{2}$/, 
	soloLetras: /^[a-zA-ZÀ-ÿ\s]{1,120}$/,
	validadcionCiRuc: /^[0-9]{10,13}$/, 
	validacionNumeroMaximoDos: /^[0-9]{0,2}$/, 
	validacionNumeroMedidor:  /^[0-9]{0,10}$/, 
}

const campos = {
	ipt_numero_ficha : false,
	ipt_num_inscripcion : false,
	ipt_codigo_actual : false,
	ipt_nombres_apellidos : false,
	ipt_direccion : false,
	ipt_lugar : false, 
	ipt_ci_ruc : false,
	ipt_provincia : false, 
	ipt_canton : false, 
	ipt_parroquia : false, 
	ipt_zona : false, 
	ipt_sector : false,
	ipt_manzana : false, 
	ipt_predio : false,
	ipt_conexion : false,
	ipt_numero_pisos : false,
	ipt_numero_personas : false,
	ipt_numero_familias : false, 
	ipt_uu_domestico : false,
	ipt_uu_publico : false,
	ipt_uu_comercial : false,
	ipt_uu_industrial : false, 
	ipt_numero_medidor : false, 
	ipt_lectura : false, 
	ipt_horas_abastecimi : false, 
	ipt_numero_cuadras : false 
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "ipt_numero_ficha":
			validarCampo(expresiones.validacionNumeroFicha, e.target, 'ipt_numero_ficha');
		break;
		case "ipt_num_inscripcion":
			validarCampo(expresiones.soloNumeros, e.target, 'ipt_num_inscripcion');
		break;
		case "ipt_codigo_actual":
			validarCampo(expresiones.validacionCodigoCatastral, e.target, 'ipt_codigo_actual');
		break;
		case "ipt_nombres_apellidos":
			validarCampo(expresiones.soloLetras, e.target, 'ipt_nombres_apellidos');
		break;
		case "ipt_direccion":
			validarCampo(expresiones.direcciones, e.target, 'ipt_direccion');
		break;
		case "ipt_lugar":
			validarCampo(expresiones.direcciones, e.target, 'ipt_lugar');
		break;
		case "ipt_ci_ruc":
			validarCampo(expresiones.validadcionCiRuc, e.target, 'ipt_ci_ruc');
		break;
		case "ipt_provincia":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_provincia');
		break;
		case "ipt_canton":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_canton');
		break;
		case "ipt_parroquia":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_parroquia');
		break;
		case "ipt_zona":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_zona');
		break;
		case "ipt_sector":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_sector');
		break;
		case "ipt_manzana":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_manzana');
		break;
		case "ipt_predio":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_predio');
		break;
		case "ipt_conexion":
			validarCampo(expresiones.validacionCodigoActual, e.target, 'ipt_conexion');
		break;
		case "ipt_numero_pisos":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_numero_pisos');
		break;
		case "ipt_numero_personas":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_numero_personas');
		break;
		case "ipt_numero_familias":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_numero_familias');
		break;
		case "ipt_uu_domestico":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_uu_domestico');
		break;
		case "ipt_uu_publico":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_uu_publico');
		break;
		case "ipt_uu_comercial":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_uu_comercial');
		break;
		case "ipt_uu_industrial":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_uu_industrial');
		break;
		case "ipt_numero_medidor":
			validarCampo(expresiones.validacionNumeroMedidor, e.target, 'ipt_numero_medidor');
		break;
		case "ipt_lectura":
			validarCampo(expresiones.validacionNumeroMedidor, e.target, 'ipt_lectura');
		break;
		case "ipt_horas_abastecimi":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_horas_abastecimi');
		break;
		case "ipt_numero_cuadras":
			validarCampo(expresiones.validacionNumeroMaximoDos, e.target, 'ipt_numero_cuadras');
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('validacion_grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('validacion_grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .validacion_input-error`).classList.remove('validacion_input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('validacion_grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('validacion_grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .validacion_input-error`).classList.add('validacion_input-error-activo');
		campos[campo] = false;
	}
}

const validarPassword2 = () => {
	const inputPassword1 = document.getElementById('password');
	const inputPassword2 = document.getElementById('password2');

	if(inputPassword1.value !== inputPassword2.value){
		document.getElementById(`grupo__password2`).classList.add('validacion_grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.remove('validacion_grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__password2 .validacion_input-error`).classList.add('validacion_input-error-activo');
		campos['password'] = false;
	} else {
		document.getElementById(`grupo__password2`).classList.remove('validacion_grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.add('validacion_grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__password2 .validacion_input-error`).classList.remove('validacion_input-error-activo');
		campos['password'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

// formulario.addEventListener('submit', (e) => {
// 	e.preventDefault();

// 	const terminos = document.getElementById('terminos');
// 	if(campos.ipt_numero_ficha && campos.ipt_num_inscripcion && campos.ipt_codigo_actual && campos.ipt_nombres_apellidos 
// 		&& campos.ipt_direccion && campos.ipt_lugar && campos.ipt_ci_ruc && campos.ipt_provincia && campos.ipt_canton 
// 		&& campos.ipt_parroquia && campos.ipt_zona && campos.ipt_sector && campos.ipt_manzana && campos.ipt_predio 
// 		&& campos.ipt_conexion && campos.ipt_numero_pisos && campos.ipt_numero_personas && campos.ipt_numero_familias 
// 		&& campos.ipt_uu_domestico && campos.ipt_uu_publico && campos.ipt_uu_comercial && campos.ipt_uu_industrial 
// 		&& campos.ipt_numero_medidor && campos.ipt_lectura && campos.ipt_horas_abastecimi && campos.ipt_numero_cuadras){
// 		e.returnValue = true;
// 		formulario.reset();

// 		document.getElementById('validacion_mensaje-exito').classList.add('validacion_mensaje-exito-activo');
// 		setTimeout(() => {
// 			document.getElementById('validacin_mensaje-exito').classList.remove('validacion_mensaje-exito-activo');
// 		}, 5000);

// 		document.querySelectorAll('.validacion_grupo-correcto').forEach((icono) => {
// 			icono.classList.remove('validacion_grupo-correcto');
// 		});
// 	} else {
// 		document.getElementById('validacion_mensaje').classList.add('validacion_mensaje-activo');
// 	}
// });

const activeEdit = document.getElementById('activeEdit');

activeEdit?.addEventListener('click', () => {
	var text_inputs =  document.getElementsByClassName("form-control");
	var text_inputs2 =  document.getElementsByClassName("validacion_input");
	var radio_buttons =  document.getElementsByClassName("form-check-input");
	var form_selects =  document.getElementsByClassName("form-select");
	enableElements(text_inputs);
	enableElements(text_inputs2);
	enableElements(radio_buttons);
	enableElements(form_selects);
	document.getElementById("edit_content").hidden = true;
	document.getElementById("exit_edit_content").hidden = false;
});

btnSaveEdit?.addEventListener("click", () => {
    if (confirm("Press a button!")) {
        document.getElementById("edit_content").hidden = false;
        document.getElementById("exit_edit_content").hidden = true;
        var text_inputs =  document.getElementsByClassName("form-control");
        var radio_buttons =  document.getElementsByClassName("form-check-input");
        var form_selects =  document.getElementsByClassName("form-select");
        disableElements(text_inputs);
        disableElements(radio_buttons);
        disableElements(form_selects);
    }
}, false);


function enableElements(args){
    for (var i = 0; i < args.length; i++) {
        args[i].disabled = false;
    }
}

function disableElements(args){
    for (var i = 0; i < args.length; i++) {
        args[i].disabled = true;
    }
}

