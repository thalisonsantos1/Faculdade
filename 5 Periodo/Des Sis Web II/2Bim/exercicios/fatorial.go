//Elabore um programa que calcule o fatorial de um número qualquer (Numero!). Exemplo: 5! = 5*4*3*2*1 = 120

package main

import "fmt"

func main() {

	var num int
	num = 5

	fatorial := 1

	for i := num; i > 0; i-- {
		fatorial = fatorial * i
	}

	fmt.Println(fatorial)
}