function calculaIMC (){
    peso = parseFloat (document.formulario.peso.value);
    altura = parseFloat (document.formulario.altura.value);
    resultado = peso/(altura * altura);
    resultado = resultado.toFixed (2);
    alert (`Seu IMC é: ${resultado}`);
}
