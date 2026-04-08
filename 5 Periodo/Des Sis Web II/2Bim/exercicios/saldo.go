//crie um programa que declare uma variável do tipo float 64
//crie funções:
//depositar (saldo *float64, valor float64)
//sacar (saldo *float64, valor float64) bool
//regras: depositar soma o valor ao saldo
// sacar subtrai o valor do saldo, se houver saldo
//no main:
// inicialize saldo = 1000
// faça um depósito
// faça um saque
// imprima o saldo final

package main

import "fmt"



func depositar(saldo *float64, valor float64) {
	*saldo += valor
}

func sacar(saldo *float64, valor float64) bool {
	if (valor > *saldo) {
		fmt.Println("Saldo insuficiente")
		return false
	} else {
		*saldo -= valor
		return true
	}
}

func main() {

	var saldo float64 = 1000.0

	depositar(&saldo, 100.0)
	fmt.Println(saldo)

	sacar(&saldo, 500.0)

	sacar(&saldo, 5000.0)
	fmt.Println(saldo)
}