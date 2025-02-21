function verificaValorLaptop(){
    var unidades = prompt ("Quantidade: ");
    qtd = unidades
    
    var preco1 = 1200
    var preco2 = 1050
    if (qtd < 5){
        var soma1 = (qtd * preco1)
        alert ("O valor total da compra é: R$ " + soma1)
    }
    else if (qtd >= 5){
        var soma2 = (qtd * preco2)
        alert ("O valor total da compra é: R$ " + soma2 + "!")
    }
}
