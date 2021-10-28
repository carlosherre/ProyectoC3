//funcion de validación login 
function loginUsuario() {

    var formLogin = document.formLogin;
    
    if (formLogin.username.value.length == 0) {
        alert('Ingrese el nombre de usuario');
        formLogin.username.value = "";
        formLogin.username.focus();
        return false;
    }
    
    if (formLogin.password.value.length == 0) {
        alert('Ingrese la contraseña');
        formLogin.password.value = "";
        formLogin.password.focus();
        return false;
    }
    
    
    formLogin.submit();
    return true
}

//funcion de validación
function validar_formulario() {

    var registroUsuario = document.getElementById('registroUsuario');
    var expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    if (registroUsuario.nombre.value.length == 0) {
        alert('Ingrese el nombre');
        registroUsuario.nombre.value = "";
        registroUsuario.nombre.focus();
        return false;
    }

    if (registroUsuario.apellido.value.length == 0) {
        alert('Ingrese el apellido');
        registroUsuario.apellido.value = "";
        registroUsuario.apellido.focus();
        return false;
    }

    console.log(expReg.test(registroUsuario.correo.value))
    if (!expReg.test(registroUsuario.correo.value)) {
        alert('Correo no valido');
        registroUsuario.correo.value = "";
        registroUsuario.correo.focus();
        return false;
    }
    if (registroUsuario.usuario.value.length < 8) {
        alert('Usuario muy corto');
        registroUsuario.usuario.value = "";
        registroUsuario.usuario.focus();
        return false;
    }
    if (registroUsuario.contrasena.value.length < 8) {
        alert('Contraseña muy corta');
        registroUsuario.contrasena.value = "";
        registroUsuario.contrasena.focus();
        return false;
    }

    if (registroUsuario.contrasena2.value.length == 0) {
        alert('Confirme la contraseña');
        registroUsuario.contrasena2.value = "";
        registroUsuario.contrasena2.focus();
        return false;
    }

    if (registroUsuario.contrasena2.value != registroUsuario.contrasena.value) {
        alert('Las contraseñas no coinciden');
        registroUsuario.contrasena2.value = "";
        registroUsuario.contrasena2.focus();
        return false;
    }

    alert('Datos enviado con exito');
    registroUsuario.submit();
    return true;

}

//funcion de validación buscar habitación 
function buscarHabitacion() {

    var busquedahabitacion = document.getElementById("busquedahabitacion");

    alert("Habitación encontrada");
    busquedahabitacion.submit();
    return true;
}

function validar_habitacion() {
    var formCreate = document.formCreate;
    if (formCreate.numero.value.length == 0) {
        alert('Ingrese el Numero de Habitacion');
        formCreate.numero.value = "";
        formCreate.numero.focus();
        return false;
    }

    if (formCreate.tipo.value == "default") {
        alert('Elija un tipo de Habitacion');
        formCreate.tipo.value = "default";
        formCreate.tipo.focus();
        return false;
    }

    if (formCreate.precio.value.length == 0) {
        alert('Ingrese un precio para la Habitacion');
        formCreate.precio.value = "";
        formCreate.precio.focus();
        return false;
    }

    if (formCreate.dispo.value.length == 0) {
        alert('Ingrese la disponibilidad de la Habitacion');
        formCreate.dispo.value = "";
        formCreate.dispo.focus();
        return false;
    }

    if (formCreate.dispoini.value.length == 0) {
        alert('Ingrese la Fecha de Inicio para la Habitacion');
        formCreate.dispoini.value = "";
        formCreate.dispoini.focus();
        return false;
    }

    if(formCreate.dispoini.value>formCreate.dispofin.value){
        alert('La fecha de inicio debe ser antes que la fecha de fin');
        formCreate.dispoini.value = "";
        formCreate.dispoini.focus();
        return false;
    }

    if (formCreate.dispofin.value.length == 0) {
        alert('Ingrese la Fecha de Fin para Habitacion');
        formCreate.dispofin.value = "";
        formCreate.dispofin.focus();
        return false;
    }
}