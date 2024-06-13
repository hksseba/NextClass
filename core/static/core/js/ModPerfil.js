$(document).ready(function() {
    const formulario = $("#FormPerfil");

    formulario.on('submit', function(e) {
        let hayErrores = false; // Variable para controlar si hay errores o no
        const errores = {}; // Objeto para almacenar todos los errores
        var foto = $("#fotoAlumno").val();

        function mostrarError(inputId, mensaje) {
            // Mostrar el mensaje de error junto al input correspondiente
            $(`#error-${inputId}`).html(mensaje);
            hayErrores = true;
            errores[inputId] = true;
        }

        // Validar longitud del nombre y apellido
        const nombre = $("#nombre").val().trim();
        if (nombre.length < 4 || nombre.length > 20) {
            mostrarError("nombre", "El nombre debe tener entre 3 y 20 caracteres.");
        }

        if (nombre.charAt(0) !== nombre.charAt(0).toUpperCase()) {
            mostrarError("nombre", "La primera letra del nombre debe ser mayúscula.");
        }

        if (!nombre.match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
            mostrarError("nombre", "El nombre no debe contener números ni caracteres especiales.");
        }

        var foto = $("#fotoPerfil").val();
        if(foto === "") {
            mostrarError("fotoPerfil", "Debe ingresar una foto.");
        }

        const apellido = $("#apellido").val().trim();
        if (apellido.length < 4 || apellido.length > 20) {
            mostrarError("apellido", "El apellido debe tener entre 4 y 20 caracteres.");
        }

        if (apellido.charAt(0) !== apellido.charAt(0).toUpperCase()) {
            mostrarError("apellido", "La primera letra del apellido debe ser mayúscula.");
        }

        if (!apellido.match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
            mostrarError("apellido", "El apellido no debe contener números ni caracteres especiales.");
        }

        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Ingrese un número.");
        } else if (/\D/.test(telefono)) {
            mostrarError("telefono", "El número no puede contener letras.");
        }

        const edad = $("#edad").val().trim();
        if (edad === "") {
            mostrarError("edad", "Ingrese una edad.");
        } else if (!/^\d+$/.test(edad)) {
            mostrarError("edad", "La edad debe ser un número.");
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
