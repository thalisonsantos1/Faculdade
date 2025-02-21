function soma (){
    var num1 = 2;
    var num2 = 5;
    var soma = 0;
    soma = num1 + num2;
    return soma;
}   

function mostraSituacao(media){
    if (media >= 7){
        alert ("Aprovado");
    } else{
        alert ("Reprovado");
    }
}

function verificaFrete (frete){
    if (frete >= 100){
        alert (0)
    }else{
        perc = frete * 0.10
        alert (perc)
    }
}

function valorTotal (unidades){
    var valor1 = 1200;
    var valor2 = 1050;
    if (unidades < 5){
        total1 = valor1 * unidades
        alert (`O total da compra é R$ ${total1}`)
    } else{
        total2 = valor2 * unidades
        alert (`O total da compra é R$ ${total2}`)
    }
}

function alerta (){
    alert ("Alerta");
}

function confirma (){
    resposta = confirm("Confirma");
    if (resposta ==1){
        return true;
    }
    else{
        return false;
    }
    
}


function entrada (){
    nome = prompt ("Digite seu nome:");
    return nome
}

function perguntaEndereco (){
    do {
        endereco = prompt ("Insira seu endereço:");
        confirma = confirm (`Seu endereço é ${endereco}!`);
    } while (!confirma);
    alert ("A página será alterada...");
    document.write (`Seu endereço é ${endereco}.`)
}





//soma ()
//mostraSituacao (8.5)
//verificaFrete (90)
//valorTotal (4)
//alerta ()
//confirma ()
//entrada ()
//perguntaEndereco ()