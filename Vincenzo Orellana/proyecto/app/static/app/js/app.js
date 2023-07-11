function validarFormulario() {
  // Obtener los valores de los campos
  var nombres = document.getElementById("nombres").value;
  var correo = document.getElementById("correo").value;
  var celular = document.getElementById("celular").value;
  var mensaje = document.getElementById("mensaje").value;

  // Validar el campo de nombres
  if (nombres.length < 4 || nombres.length > 16) {
    alert("El nombre debe tener entre 4 y 16 caracteres.");
    return false;
  }

  // Validar el campo de correo
  var correoRegex = /^[\w-]+(\.[\w-]+)*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*(\.[a-zA-Z]{2,})$/;
  if (!correoRegex.test(correo)) {
    alert("Por favor, ingresa un correo válido.");
    return false;
  }

  // Validar el campo de celular
  var celularRegex = /^\d{10}$/;
  if (!celularRegex.test(celular)) {
    alert("Por favor, ingresa un número de celular válido (10 dígitos).");
    return false;
  }

  // Validar el campo de mensaje
  var palabras = mensaje.trim().split(" ");
  if (palabras.length > 200) {
    alert("El mensaje no puede exceder las 200 palabras.");
    return false;
  }

  // Si todos los campos son válidos, se puede enviar el formulario
  return true;
}


function iniciarMap(){
  var coord = {lat:-34.5956145 ,lng: -58.4431949};
  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 10,
    center: coord
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map
  });
}