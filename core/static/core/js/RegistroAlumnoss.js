$(document).ready(function() {
    const formulario = $("#formregistro");

    // Mostrar el campo de correo de los padres si la edad es menor de 18
    $("#edad").on('input', function() {
        const edad = parseInt($(this).val());
        if (!isNaN(edad) && edad < 18) {
            $("#labelpolla").show();
            $("#correo_padres").show();
        } else {
            $("#labelpolla").hide();
            $("#correo_padres").hide();
        }
    });

    formulario.on('submit', function(e) {
        // Prevenir el envío del formulario por defecto
        let hayErrores = false; // Variable para controlar si hay errores o no
        const errores = {}; // Objeto para almacenar todos los errores

        function mostrarError(inputId, mensaje) {
            // Mostrar el mensaje de error junto al input correspondiente
            $(`#error-${inputId}`).html(mensaje);
            hayErrores = true;
            errores[inputId] = true;
        }

        function validarCorreo(correo) {
            var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return regex.test(correo);
        }

        // Validar longitud del nombre y apellido
        const nombre = $("#nombre").val().trim();
        if (nombre.length < 4 || nombre.length > 20) {
            mostrarError("nombre", "El nombre debe tener entre 4 y 20 caracteres.");
        }

        if (nombre.charAt(0) !== nombre.charAt(0).toUpperCase()) {
            mostrarError("nombre", "La primera letra del nombre debe ser mayúscula.");
        }

        if (!nombre.match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
            mostrarError("nombre", "El nombre no debe contener números ni caracteres especiales.");
        }

        var foto = $("#fotoAlumno").val();
        if (foto === "") {
            mostrarError("fotoAlumno", "Debe ingresar una foto.");
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

        const correo = $("#email").val().trim();
        if (!validarCorreo(correo)) {
            mostrarError("email", "El correo electrónico no es válido.");
        }

        if (correo === "") {
            mostrarError("email", "Por favor, ingrese su correo electrónico.");
        }

        var sexo = $("#sexo").val();
        if (sexo === "") {
            mostrarError("sexo", "Por favor, ingrese su sexo.");
        }

        const clave = $("#contrasena").val();
        if (clave.length < 8 || clave.length > 25) {
            mostrarError("contrasena", "La contraseña debe tener entre 8 y 25 caracteres.");
        }

        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Ingrese un número.");
        } else if (/\D/.test(telefono)) {
            mostrarError("telefono", "El número no puede contener letras.");
        }

        const NvlEducativo = $("#NvlEducativo").val().trim();
        if (NvlEducativo === "") {
            mostrarError("NvlEducativo", "Debe seleccionar una opción.");
        }

        // Validar la edad y mostrar el campo de correo de los padres si es necesario
        const edad = parseInt($("#edad").val());
        if (isNaN(edad) || edad < 0 || edad > 150) {
            mostrarError("edad", "La edad ingresada no es válida.");
        } else if (edad < 18) {
            $("#labelpolla").show();
            $("#correo_padres").show();
        } else {
            $("#labelpolla").hide();
            $("#correo_padres").hide();
        }

        // Validar correo de los padres si la edad es menor de 18
        if (edad < 18) {
            const correoPadres = $("#correo_padres").val().trim();
            if (!validarCorreo(correoPadres)) {
                mostrarError("correo_padres", "El correo electrónico de los padres no es válido.");
            }

            if (correoPadres === "") {
                mostrarError("correo_padres", "Por favor, ingrese el correo electrónico de los padres.");
            }
        }

        if (hayErrores) {
            e.preventDefault(); // Evitar el envío del formulario si hay errores
        }
    });
});