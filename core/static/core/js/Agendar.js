// JavaScript - Agendar.js
$(document).ready(function() {
    $("#datepicker").hide();
    $("#timepicker").hide();

    $("#datepicker").datepicker({
        minDate: 0,
        dateFormat: 'dd/mm/yy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sá'],
        onSelect: function() {
            $("#timepicker").show();
            $("#timepicker").timepicker({
                timeFormat: 'HH:mm',
                interval: 30,
                minTime: '6:00am',
                maxTime: '10:00pm',
                defaultTime: '8:00am',
                startTime: '6:00am',
                dynamic: false,
                dropdown: true,
                scrollbar: true,
                onSelect: function() {
                    $("#agendar").show();
                    $("#pagarBtn").show();  // Mostrar el botón de pagar después de seleccionar la hora
                }
            });
        }
    });

    $("#btn1").click(function() {
        $("#btn1").addClass("active");
        $("#btn2").removeClass("active");
        $("#datepicker").hide();
        $("#timepicker").hide();
        $("#agendar").show();
    });

    $("#btn2").click(function() {
        $("#btn2").addClass("active");
        $("#btn1").removeClass("active");
        $("#datepicker").show();

    });
});

function verificarDisponibilidad() {
    var fechaSeleccionada = $('#datepicker').val();
    var horaSeleccionada = $('#timepicker').val();
    var claseId = $('#id_clase').val();
    console.log('Fecha seleccionada:', fechaSeleccionada);
    console.log('Hora seleccionada:', horaSeleccionada);
    console.log('Clase ID:', claseId);

    $.ajax({
        url: 'http://127.0.0.1:8000/api/verificar_disponibilidad/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            fecha: fechaSeleccionada,
            hora: horaSeleccionada,
            clase_id: claseId,
        }),
        success: function(data) {
            console.log('Respuesta del servidor:', data);
            if (data.disponible) {
                crearSesion();
            } else {
                alert('La hora ya está ocupada. Por favor, elige otra hora.');
            }
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}

$(document).ready(function() {
    $('#datepicker').datepicker({
        dateFormat: 'yy-mm-dd'
    });
    $('#timepicker').timepicker({
        timeFormat: 'HH:mm'
    });
});

function crearSesion() {
    var fechaSeleccionada = $('#datepicker').val();
    var horaSeleccionada = $('#timepicker').val();
    var claseId = $('#id_clase').val();
    var telefono = $('#telefono').val();
    var mensaje = $('#msg').val();
    var profe = $('#id_profesor').val();
    var estudiante = $('#id_alumno').val();

    console.log('Fecha seleccionada:', fechaSeleccionada);
    console.log('Hora seleccionada:', horaSeleccionada);
    console.log('ID de clase:', claseId);
    console.log('Teléfono:', telefono);
    console.log('Mensaje:', mensaje);
    console.log('Id del profe', profe);
    console.log('Id del estudiante', estudiante);

    // Verificar si los valores de fecha y hora están presentes y no están vacíos
    if (!fechaSeleccionada || !horaSeleccionada) {
        alert('Por favor, selecciona una fecha y una hora.');
        return;
    }

    // Dividir fecha y hora en componentes para construir un objeto Date
    var fechaComponentes = fechaSeleccionada.split('/');
    var horaComponentes = horaSeleccionada.split(':');

    // Construir el objeto Date en formato correcto (mes - 1 porque en JavaScript los meses son de 0 a 11)
    var fechaHora = new Date(fechaComponentes[2], fechaComponentes[1] - 1, fechaComponentes[0], horaComponentes[0], horaComponentes[1]);

    // Verificar si la fecha y hora son válidas
    if (isNaN(fechaHora.getTime())) {
        alert('Fecha u hora inválidas. Por favor, revisa las entradas.');
        return;
    }

    // Ajustar la fecha y hora a la zona horaria de Santiago, Chile
    var fechaHoraSantiago = new Date(fechaHora.toLocaleString('en-US', { timeZone: 'America/Santiago' }));

    // Convertir a formato ISO 8601
    var fechaHoraISO = fechaHoraSantiago.toISOString();
    console.log('FECHA FINAL', fechaHoraISO);

    $.ajax({
        url: 'http://127.0.0.1:8000/api/crear_sesion/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            fechaclase: fechaHoraISO,
            clase: claseId,
            telefono: telefono,
            mensaje: mensaje,
            profesor: profe,
            estudiante: estudiante,
            estado_pago: false
        }),
        success: function(response) {
            console.log('Sesión creada:', response);
            alert('Sesión creada exitosamente.');
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}
