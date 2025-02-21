function freteKm(){
    valorKm = parseFloat (document.formulario.valorKm.value);
    qtdKm = parseFloat (document.formulario.qtdKm.value);
    valorFrete = (valorKm*qtdKm);
    valorFrete = valorFrete.toFixed (2);    
    alert (`O valor do frete é R$ ${valorFrete}!`);
}