const nota = prompt("Digite a nota do aluno: ")
    if (nota <= 100 && nota >= 90){
        alert ("Parabéns! Esse aluno é nota A!!!")
    } else if (nota < 90 && nota >= 80){
        alert ("Parabéns! Esse aluno é nota B!!!")
    } else if (nota < 80 && nota >= 70){
        alert ("Esse aluno é nota C!!!")
    } else if (nota < 70 && nota >= 60){
        alert ("Esse aluno é nota D!!!")
    } else {
        alert (" Infelizmente esse aluno é nota F!!!")
    } 