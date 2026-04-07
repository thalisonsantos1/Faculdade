//Bill tem 1.85 bilhões (1850 milhões) na sua conta e Jeff tem 1.65 bilhões(1650 milhões). Porém Bill aumenta o seu saldo em 20 milhões por ano, enquanto Jeff aumenta 28 milhões ao ano. Calcule quantos anos demorará para Jeff ficar mais rico que Bill.

package main

import "fmt"

func main() {

	var bill float64 = 185000000000
	var jeff float64 = 165000000000
	var anos int = 0

	for jeff <= bill {
		bill += 20000000
		jeff += 28000000
		anos++
	}

	fmt.Println(anos, "anos")
	}