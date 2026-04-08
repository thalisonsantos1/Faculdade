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

// fazer método transferir, levando dinheiro de uma conta para outra

package main

import "fmt"

type Conta struct {
	correntista string
	saldo float64
}

func main() {

	c := Conta{}
	c.correntista = "Joao"
	c.saldo = 1000.0
	c.depositar(500)
	c.sacar(250)
	c.sacar(2000)
	c2 := Conta{}
	c.transferir(&c2, 500)
	fmt.Println("Saldo conta 1:", c.saldo, "Saldo conta 2:", c2.saldo)
	
}

func (c *Conta) depositar(valor float64) {
	c.saldo += valor
}

func (c *Conta) sacar(valor float64) bool {
	if (valor > c.saldo) {
		fmt.Println("Saldo insuficiente")
		return false
	} else {
		c.saldo -= valor
		return true
	}
}

func (c *Conta) transferir(outra *Conta, valor float64) bool {
	if valor > c.saldo {
		fmt.Println("Saldo insuficiente")
		return false
	} else {
		c.saldo -= valor
		outra.saldo += valor
		return true
	}
}





