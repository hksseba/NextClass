$(document).ready(function() {
    const formulario = $("#registroP");

    formulario.on('submit', function(e) {
        // Prevenir el envío del formulario por defecto
        e.preventDefault();

        let hayErrores = false; // Variable para controlar si hay errores o no

        function mostrarError(inputId, mensaje) {
            // Mostrar el mensaje de error debajo del input correspondiente
            $(`#error-${inputId}`).html(mensaje);
            hayErrores = true;
        }

        // Resto del código de validación...

        const run = $("#run_profe").val().trim();
        if (run === "") {
            mostrarError("run_profe", "Debe ingresar un RUN.");
        }

        const foto = $("#foto_profe").val();
        if (foto === "") {
            mostrarError("foto_profe", "Debe ingresar una foto.");
        }

        // const antecedentes = $("#antecedentes").val();
        // if (antecedentes === "") {
        //     mostrarError("antecedentes", "Debe ingresar antecedentes.");
        // }

        const nombre = $("#nombre").val().trim();
        if (nombre === "") {
            mostrarError("nombre", "Debe ingresar su nombre.");
        }

        const apellido = $("#apellido").val().trim();
        if (apellido === "") {
            mostrarError("apellido", "Debe ingresar su apellido.");
        }

        const edad = $("#edad").val().trim();
        if (edad === "") {
            mostrarError("edad", "Debe ingresar su edad.");
        }

        const email = $("#email").val().trim();
        if (email === "") {
            mostrarError("email", "Debe ingresar su correo electrónico.");
        }

        const contra = $("#contra").val();
        if (contra === "") {
            mostrarError("contra", "Debe ingresar una contraseña.");
        }

        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Debe ingresar su número de teléfono.");
        }

        const tarifa = $("#tarifa").val().trim();
        if (tarifa === "") {
            mostrarError("tarifa", "Debe ingresar una tarifa.");
        }

        const especializacion = $("select[name='especializacion']").val();
        if (especializacion === "") {
            mostrarError("especializacion", "Debe seleccionar una especialización.");
        }

        const descripcion = $("textarea[name='descripcion']").val().trim();
        if (descripcion === "") {
            mostrarError("descripcion", "Debe ingresar una descripción.");
        }

        // Si hay errores, detener el proceso y mostrar todos los errores
        if (hayErrores) {
            return; // Detiene la ejecución del formulario
        } else {
            // Si no hay errores, enviar el formulario
            formulario.unbind('submit').submit();
        }
    });
});