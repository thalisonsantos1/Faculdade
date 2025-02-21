const idade = prompt("Digite a idade do Cliente: ")
    if (idade < 18){
        alert ("O desconto para esse cliente é de 20%!")
    } else if (idade >= 18 && idade < 60){
        alert ("O desconto para esse cliente é de 10%!")
    } else{
        alert ("Infelizmente esse cliente não tem direito a desconto")
    } 