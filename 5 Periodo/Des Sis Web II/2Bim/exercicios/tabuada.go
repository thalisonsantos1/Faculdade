//Faça um algoritmo que declare uma variável com um número qualquer. Mostre a tabuada desse número.

package main

import "fmt"

func main() {

	var num int
	num = 7

	for i := 1; i <= 10; i++ {
		fmt.Println(num * i)
	}
}