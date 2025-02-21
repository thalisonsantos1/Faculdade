let contador = 1;
while (contador <= 5){
    console.log ("Numero" + contador)
    contador ++;
}

//----------------------------------------------

let resposta = "sim"
while (resposta === "sim"){
    console.log ("Resposta correta!");
    resposta = prompt ("Digite 'sim' para continuar ou qualquer outro valor para sair")
}

//----------------------------------------------

let base = prompt ("Digite o valor desejado: ")
let expoente = 3;
while(expoente <= 3){
    console.log (`${base} elevado a ${expoente} é:` , Math.pow(base, expoente));
    expoente += 1;
}

//---------------------------------------------------


let frutas = ["maçã", "banana", "manga"];
let indice = 0;
while (indice <= (frutas.length) - 1){;
console.log (`eu gosto de ${frutas[indice]}`);
indice += 1;
}
//--------------------------------------------------

let msg = "";
let j = 0;
do {
    msg += j + "\n";
    j++
} while (j <= 10);
console.log (msg)

//----------------------------------------------------

const Carro = {
    marca: "Renaut",
    modelo: "Logan",
    comprimento: "4.250mm",
    largura: "1.735mm",
    altura: "1.525mm",
};
let msg2 = "", k;
for (k in Carro){
    msg2 += k + ":" + Carro[k]+ "\n";
}
console.log (msg2);