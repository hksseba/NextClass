$(document).ready(function() {
    const formulario = $("#registroP");

    formulario.on('submit', function(e) {
        // Prevenir el envío del formulario por defecto
      

        let hayErrores = false; // Variable para controlar si hay errores o no

        function mostrarError(inputId, mensaje) {
            // Mostrar el mensaje de error debajo del input correspondiente
            $(`#error-${inputId}`).html(mensaje);
            hayErrores = true;
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

       

        var rut = $('#run_profe').val().trim();
        if (!validarRut(rut)) {
            mostrarError("run_profe", "Debe ingresar un RUN valido.");
        
        } 

        const run = $("#run_profe").val().trim();
        if (run === "") {
            mostrarError("run_profe", "Debe ingresar un RUN.");
        }

        const foto = $("#foto_profe").val();
        if (foto === "") {
            mostrarError("foto_profe", "Debe ingresar una foto.");
        }

         const antecedentes = $("#antecedentes").val();
         if (antecedentes === "") {
             mostrarError("antecedentes", "Debe ingresar antecedentes.");
         }

         const carnet = $("#carnet").val();
         if (carnet === "") {
             mostrarError("carnet", "Debe ingresar su carnet de identidad.");
         }

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

        const correo = $("#email").val().trim();
      if (!validarCorreo(correo)) {
          mostrarError("email", "El correo electrónico no es válido.");
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
            e.preventDefault()
        } else {
            // Si no hay errores, enviar el formulario
            formulario.unbind('submit').submit();
        }
    });
});