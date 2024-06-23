$(document).ready(function() {
    const formulario = $("Calificar");

    formulario.on('submit', function(e) {
        

        let hayErrores = false; // Variable para controlar si hay errores o no
        const errores = {}; // Objeto para almacenar todos los errores

        function mostrarError(inputId, mensaje) {
            // Mostrar el mensaje de error debajo del input correspondiente
            $(`#error-${inputId}`).html(mensaje);
            hayErrores = true;
            errores[inputId] = true;
        }

        function limpiarError(inputId) {
            // Limpiar el mensaje de error del input correspondiente
            $(`#error-${inputId}`).html('');
            delete errores[inputId];
        }


        const calificacion = $("#calificacion").val();
        if (calificacion === "") {
            mostrarError("calificacion", "Debe ingresar una valoracion.");
        } else {
            limpiarError("calificacion");
        }

        const comentario = $("#comentario").val();
        if (comentario === "") {
            mostrarError("comentario", "Debe ingresar un comentario.");
        } else {
            limpiarError("comentario");
        }


        // Si hay errores, detener el proceso y mostrar todos los errores
        if (hayErrores) {
            e.preventDefault();
        } else {
            // Si no hay errores, enviar el formulario
            formulario.unbind('submit').submit();
        }
    });
});