$(document).ready(function() {
    const formulario = $("#registroAdmin");

    formulario.on('submit', function(e) {
        e.preventDefault(); // Prevenir el envío del formulario por defecto

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

        function validarCorreo(correo) {
            var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return regex.test(correo);
        }

        function validarContrasena(contra) {
            const mensajesError = [];

            if (contra.length < 8 || contra.length > 25) {
                mensajesError.push("La contraseña debe tener entre 8 y 25 caracteres.");
            }
            if (!/[A-Z]/.test(contra)) {
                mensajesError.push("La contraseña debe contener al menos una letra mayúscula.");
            }
            if (!/[a-z]/.test(contra)) {
                mensajesError.push("La contraseña debe contener al menos una letra minúscula.");
            }
            if (!/[0-9]/.test(contra)) {
                mensajesError.push("La contraseña debe contener al menos un número.");
            }
            if (!/[!@#$%^&*()='?¿¡+~{}^,.-;:_¬|°]/.test(contra)) {
                mensajesError.push("La contraseña debe contener al menos un carácter especial (!@#$%^&*()='?¿¡+~{}^,.-;:_¬|°).");
            }

            return mensajesError;
        }

        // Validaciones
        const nombre = $("#nombre").val().trim();
        if (nombre === "") {
            mostrarError("nombre", "Debe ingresar su nombre.");
        } else {
            limpiarError("nombre");
        }

        const apellido = $("#apellido").val().trim();
        if (apellido === "") {
            mostrarError("apellido", "Debe ingresar su apellido.");
        } else {
            limpiarError("apellido");
        }

        const correo = $("#email").val().trim();
        if (!validarCorreo(correo)) {
            mostrarError("email", "El correo electrónico no es válido.");
        } else if (correo === "") {
            mostrarError("email", "Por favor, ingrese su correo electrónico.");
        } else {
            limpiarError("email");
        }

        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Debe ingresar su número de teléfono.");
        } else {
            limpiarError("telefono");
        }

        const contra = $("#contra").val();
        const erroresContrasena = validarContrasena(contra);
        if (erroresContrasena.length > 0) {
            mostrarError("contra", erroresContrasena.join("<br>"));
        } else {
            limpiarError("contra");
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