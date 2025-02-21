let escapaClosure;

function funcaoExterna(){
    alert ("Função Externa");
    function funcaoInterna (){
        alert ("Função Interna");
    }
    escapaClosure = funcaoInterna;
}
