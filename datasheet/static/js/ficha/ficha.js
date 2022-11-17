function ListadoFichas(){
    $.ajax({
        url: "/ficha/list-datasheet/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if ($.fn.DataTable.isDataTable('#tabla_fichas')) {
                $('#tabla_fichas').DataTable().destroy();
            }
            $('#tabla_fichas tbody').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]["numero_ficha"] + '</td>';
                fila += '<td>' + response[i]["cedula_identidad"] + '</td>';
                fila += '<td>' + response[i]["clave_catastral_actual"] + '</td>';
                fila += '<td>' + response[i]["nuevo_codigo_catastral"] + '</td>';
                fila += '<td>' + response[i]["fecha_encuesta"] + '</td>';
                fila += '<td>' + response[i]["observaciones"] + '</td>';
                // if (response[i]["fields"]['autor_id'] == ''){
                //     fila += '<td>Desconocido</td>';
                // }else{
                //     fila += '<td>' + response[i]["fields"]['autor_id'] + '</td>';       
                // }                
                fila += '<td><a class="btn btn-primary btn-sm tableButton mt-2 mx-2"';
                fila += ' href="/ficha/edit-datasheet/' + response[i]['id'] + '/"> EDITAR </a>';
                fila += '<button type = "button" class="btn btn-danger tableButton mt-2 btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/ficha/delete-datasheet/' + response[i]['id'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';
                $('#tabla_fichas tbody').append(fila);
            }
            $('#tabla_fichas').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                        "first": "Primero",
                        "last": "Ultimo",
                        "next": "Siguiente",
                        "previous": "Anterior"
                    },
                },
            });
        },
        error: function (error) {
            console.log(error);
        }
    });
}

$(document).ready(function(){
    ListadoFichas(); 
});

function EliminarFicha(id){
    Swal.fire({
        "title":"¿Estás seguro?",
        "text":"Ésta acción no se puede deshacer",
        "icon":"question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar",
        "confirmButtonText":"Si, Eliminar", 
        "reverseButtons":true,
        "confirmButtonColor":"#dc3545"
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/ficha/delete-datasheet/"+id+"/"
        }
    })
}

function eliminarFicha(pk) {
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/ficha/delete-datasheet/' + pk + '/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            ListadoFichas();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}