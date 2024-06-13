$(document).ready(function() {
    const formulario = $("#formregistro");

    function mostrarError(inputId, mensaje) {
        $(`#error-${inputId}`).html(mensaje);
    }

    function limpiarError(inputId) {
        $(`#error-${inputId}`).html('');
    }

    function validarCorreo(correo) {
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
    }

    function validarContrasena(contrasena) {
        const errores = [];
        if (contrasena.length < 8 || contrasena.length > 25) {
            errores.push("La contraseña debe tener entre 8 y 25 caracteres.");
        }
        if (!/[A-Z]/.test(contrasena)) {
            errores.push("La contraseña debe incluir al menos una letra mayúscula.");
        }
        if (!/[a-z]/.test(contrasena)) {
            errores.push("La contraseña debe incluir al menos una letra minúscula.");
        }
        if (!/\d/.test(contrasena)) {
            errores.push("La contraseña debe incluir al menos un número.");
        }
        if (!/[!@#$%^&*()='?¿¡+~{}^,.-;:_¬|°]/.test(contrasena)) {
            errores.push("La contraseña debe incluir al menos un carácter especial (!@#$%^&*()='?¿¡+~{}^,.-;:_¬|°).");
        }
        return errores;
    }

    function validarCampos() {
        let hayErrores = false;

        // Validar Foto
        var foto = $("#fotoAlumno").val();
        if (foto === "") {
            mostrarError("fotoAlumno", "Debe ingresar una foto.");
            hayErrores = true;
        } else {
            limpiarError("fotoAlumno");
        }

        // Validar Sexo
        const sexo = $("#sexo").val().trim();
        if (sexo === "") {
            mostrarError("Sexo", "Debe seleccionar una opción.");
            hayErrores = true;
        } else {
            limpiarError("Sexo");
        }

        // Validar Nombre
        const nombre = $("#nombre").val().trim();
        if (nombre.length < 4 || nombre.length > 20) {
            mostrarError("nombre", "El nombre debe tener entre 4 y 20 caracteres.");
            hayErrores = true;
        } else if (nombre.charAt(0) !== nombre.charAt(0).toUpperCase()) {
            mostrarError("nombre", "La primera letra del nombre debe ser mayúscula.");
            hayErrores = true;
        } else if (!nombre.match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
            mostrarError("nombre", "El nombre no debe contener números ni caracteres especiales.");
            hayErrores = true;
        } else {
            limpiarError("nombre");
        }

        // Validar Apellido
        const apellido = $("#apellido").val().trim();
        if (apellido.length < 4 || apellido.length > 20) {
            mostrarError("apellido", "El apellido debe tener entre 4 y 20 caracteres.");
            hayErrores = true;
        } else if (apellido.charAt(0) !== apellido.charAt(0).toUpperCase()) {
            mostrarError("apellido", "La primera letra del apellido debe ser mayúscula.");
            hayErrores = true;
        } else if (!apellido.match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
            mostrarError("apellido", "El apellido no debe contener números ni caracteres especiales.");
            hayErrores = true;
        } else {
            limpiarError("apellido");
        }

        // Validar Correo Electrónico
        const correo = $("#email").val().trim();
        if (correo === "") {
            mostrarError("email", "Por favor, ingrese su correo electrónico.");
            hayErrores = true;
        } else if (!validarCorreo(correo)) {
            mostrarError("email", "El correo electrónico no es válido.");
            hayErrores = true;
        } else {
            limpiarError("email");
        }

        // Validar Contraseña
        const clave = $("#contrasena").val();
        const erroresContrasena = validarContrasena(clave);
        if (erroresContrasena.length > 0) {
            mostrarError("contrasena", erroresContrasena.join('<br>'));
            hayErrores = true;
        } else {
            limpiarError("contrasena");
        }

        // Validar Teléfono
        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            mostrarError("telefono", "Ingrese un número.");
            hayErrores = true;
        } else if (/\D/.test(telefono)) {
            mostrarError("telefono", "El número no puede contener letras.");
            hayErrores = true;
        } else {
            limpiarError("telefono");
        }

        // Validar Nivel Educativo
        const NvlEducativo = $("#NvlEducativo").val().trim();
        if (NvlEducativo === "") {
            mostrarError("NvlEducativo", "Debe seleccionar una opción.");
            hayErrores = true;
        } else {
            limpiarError("NvlEducativo");
        }

        return !hayErrores;
    }

    // Validación en tiempo real
    $("#formregistro input, #formregistro select").on('input change', function() {
        validarCampos();
    });

    formulario.on('submit', function(e) {
        if (!validarCampos()) {
            e.preventDefault();
        }
    });
});