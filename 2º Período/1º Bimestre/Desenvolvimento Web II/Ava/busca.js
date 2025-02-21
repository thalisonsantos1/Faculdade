function valida (){
    if (document.formulario.busca.value == ""){
        alert ("Preencha o campo BUSCA corretamente");
        document.formulario.busca.focus ();
        return false;
    }
    if (document.formulario.busca.value.length < 3){
        alert ("Informe pelo menos 3 letras!");
        document.formulario.busca.focus();
        return false
    }
    return true;
}