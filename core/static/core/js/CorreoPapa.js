$(document).ready(function() {
    const formulario = $("#formcorreo");
  
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
          
        const correo = $("#correo").val().trim();
        if (!validarCorreo(correo)) {
            mostrarError("correo", "El correo electrónico no es válido.");
        }    
  
        if (correo === "") {
            mostrarError("correo", "Por favor, ingrese su correo electrónico.");
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
  