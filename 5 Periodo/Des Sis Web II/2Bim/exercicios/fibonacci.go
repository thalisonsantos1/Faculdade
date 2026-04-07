//A série de Fibonacci é formada pela seguinte seqüência: 0,1,1,2,3,5,8,13,21,34,55... etc. Escreva um algoritmo que gere a série de Fibonacci até o vigésimo termo utilizando uma estrutura de repetição.

package main

import "fmt"

func main() {

	var num1 int = 0
	var num2 int = 1
	var num3 int = 0

	for i := 0; i < 20; i++ {
		num3 = num1 + num2
		num1 = num2
		num2 = num3
		fmt.Println(num3)
	}
}