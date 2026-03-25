package main

import "fmt"

func main() {
	//var produto string
	var qtd float64
	var preco float64
	var desconto float64

	//produto = "Notebook"
	qtd = 4
	preco = 1899.90
	//qtdTotal = 6
	desconto = 0.1

	if qtd < 5 {
		valorTotal := qtd * preco
		fmt.Println("O valor total é: ", valorTotal)
	}

	if qtd >= 5 {
		valorTotal := qtd * preco * (1 - desconto)
		fmt.Println("O valor total é: ", valorTotal)
	} 
	
}