document.addEventListener("DOMContentLoaded", function() {
    // Ocultar el Datepicker cuando se carga la página
    $("#datepicker").hide();

    // Inicializar el Datepicker
    $(function() {
        $("#datepicker").datepicker({
            minDate: 0, // Establecer la fecha mínima como hoy
            dateFormat: 'dd/mm/yy', // Establecer el formato de fecha en español
            monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sá'] // Establecer los nombres de los días de la semana en español
        });
    });

    // Manejar el clic en el botón "Lo antes posible"
    document.getElementById("btn1").addEventListener("click", function() {
        document.getElementById("btn1").classList.add("active");
        document.getElementById("btn2").classList.remove("active");

        // Ocultar el Datepicker
        $("#datepicker").hide();
    });

    // Manejar el clic en el botón "Propón una fecha"
    document.getElementById("btn2").addEventListener("click", function() {
        document.getElementById("btn2").classList.add("active");
        document.getElementById("btn1").classList.remove("active");

        // Mostrar el Datepicker
        $("#datepicker").show();
    });
});
