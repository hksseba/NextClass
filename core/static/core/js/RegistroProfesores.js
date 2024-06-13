$(document).ready(function() {
    const formulario = $("#registroP");

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

        function validarRut(rut) {
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) return false;
            var parts = rut.split('-');
            var body = parts[0];
            var dv = parts[1].toUpperCase();
            var rutDigits = body.split('').reverse().join('');
            var sum = 0;
            for (var i = 0; i < rutDigits.length; i++) {
                sum += parseInt(rutDigits[i]) * (i % 6 + 2);
            }
            var mod = sum % 11;
            var expectedDV = mod === 0 ? 0 : 11 - mod;
            if (expectedDV === 10) expectedDV = 'K';
            return expectedDV == dv;
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
        const run = $("#run_profe").val().trim();
        if (!validarRut(run)) {
            mostrarError("run_profe", "Debe ingresar un RUN válido.");
        } else {
            limpiarError("run_profe");
        }

        const foto = $("#foto_profe").val();
        if (foto === "") {
            mostrarError("foto_profe", "Debe ingresar una foto.");
        } else {
            limpiarError("foto_profe");
        }

        const antecedentes = $("#antecedentes").val();
        if (antecedentes === "") {
            mostrarError("antecedentes", "Debe ingresar antecedentes.");
        } else {
            limpiarError("antecedentes");
        }

        const carnet = $("#carnet").val();
        if (carnet === "") {
            mostrarError("carnet", "Debe ingresar su carnet de identidad.");
        } else {
            limpiarError("carnet");
        }

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

        const edad = $("#edad").val().trim();
        if (edad === "") {
            mostrarError("edad", "Debe ingresar su edad.");
        } else {
            limpiarError("edad");
        }

        const correo = $("#email").val().trim();
        if (!validarCorreo(correo)) {
            mostrarError("email", "El correo electrónico no es válido.");
        } else if (correo === "") {
            mostrarError("email", "Por favor, ingrese su correo electrónico.");
        } else {
            limpiarError("email");
        }

        const contra = $("#contra").val();
        const erroresContrasena = validarContrasena(contra);
        if (erroresContrasena.length > 0) {
            mostrarError("contra", erroresContrasena.join("<br>"));
        } else {
            limpiarError("contra");
        }

        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Debe ingresar su número de teléfono.");
        } else {
            limpiarError("telefono");
        }

        const especializacion = $("select[name='especializacion']").val();
        if (especializacion === "") {
            mostrarError("especializacion", "Debe seleccionar una especialización.");
        } else {
            limpiarError("especializacion");
        }

        const descripcion = $("textarea[name='descripcion']").val().trim();
        if (descripcion === "") {
            mostrarError("descripcion", "Debe ingresar una descripción.");
        } else {
            limpiarError("descripcion");
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