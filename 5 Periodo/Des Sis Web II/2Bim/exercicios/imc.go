//Declare variáveis para a sua altura e peso. calcule o seu IMC através da fórmula (IMC = peso/(altura*altura)). Mostre uma mensagem de que a pessoa está com peso correto quando o IMC for menor que 25, e informe que está de sobrepeso caso contrário.

package main

import "fmt"

func main() {
	

	var altura float64
	var peso float64	
	var imc float64

	altura = 1.70
	peso = 80.0
	imc = peso / (altura * altura)

	if imc < 25 {
		fmt.Println("Peso correto")
	} else {
		fmt.Println("Sobrepeso")
	}
}
