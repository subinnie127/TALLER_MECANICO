//aqui se colocan todas las variables//
var rut = document.getElementById('rut');
var nombres = document.getElementById('nombres'); 
var apellidos = document.getElementById('apellidos');
var correo = document.getElementById('correo');
var direccion = document.getElementById('direccion');
var foto = document.getElementById('foto');
var contra = document.getElementById('contra');
var recontra = document.getElementById('recontra');
var error = document.getElementById('error');
var succes = document.getElementById('succes');
var z;

var boton = document.querySelectorAll(".btn");
var mostrarC = document.querySelectorAll(".no_mostrar");

boton.forEach(function(elemento,indice){
    elemento.addEventListener("click",function(){
        mostrarC[indice].classList.toggle("mostrarC");
        if(mostrarC[indice].classList.contains("mostrarC")){
            elemento.innerHTML = "Ocultar";
        }else{
                elemento.innerHTML = "Mostrar descripción ";
        }   
    });
})



//script del registro con sus respectivos parametros de validacion


//registro
function registrar(){
    console.log('enviando datos desde js')

    var mensaje = [];
    

    if(rut.value===null || rut.value===''){
        mensaje.push('debe ingresar un rut')
        z=false
    }else{
        z=true
    }

    if(nombres.value===null || nombres.value===''){
        mensaje.push('debe ingresar algun nombre')
        z=false
    }else{
        z=true
    }

    if(apellidos.value===null || apellidos.value===''){
        mensaje.push('debe ingresar algun apellido')
        z=false
    }else{
        z=true
    }

    if(correo.value===null || correo.value===''){
        mensaje.push('debe ingresar algun correo')
        z=false
    }else{
        z=true
    }

    if(direccion.value===null || direccion.value===''){
        mensaje.push('debe ingresar alguna direccion')
        z=false
    }else{
        z=true
    }

    if(foto.value===null || foto.value===''){
        z=false
    }else{
        z=true
    }

    if(contra.value===null || contra.value===''){
        mensaje.push('debe ingresar una contraseña')
        z=false
    }else{
        z=true
    }

    if(recontra.value===null || recontra.value==='' || recontra.value!==contra.value){
        mensaje.push('las contraseñas no coinciden')
        z=false
    }else{
        z=true
    }

    //validacion de datos requeridos para mostrar un mensaje de registro completado a traves de una variable z
    if(z!==true){
        error.innerHTML=mensaje.join(' || ');
    }else{
        succes.style.display = 'block';
        error.style.display = 'none';
    }

    return false;
}