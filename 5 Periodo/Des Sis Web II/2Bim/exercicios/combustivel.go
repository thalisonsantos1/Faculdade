//considere que um carro faz 9km/litro de consumo com alcool. Já na gasolina ele faz 11km/litro. Faça um algoritmo que declare variáveis para a distância que deseja viajar, o preço do alcool e o preço do litro da gasolina. Calcule e mostre o valor que será gasto caso abasteça com alcool e o valor gasto com gasolina.  Mostre ainda se compensa abastecer com alcool ou com gasolina.

package main

import "fmt"

func main() {

	var distancia float64
	var mediaAlcool float64
	var mediaGasolina float64
	var consumoAlcool float64
	var consumoGasolina float64
	var precoAlcool float64
	var precoGasolina float64
	var gastoAlcool float64
	var gastoGasolina float64

	distancia = 100.0
	precoAlcool = 4.60
	precoGasolina = 6.89
	mediaAlcool = 9.0
	mediaGasolina = 11.0

	consumoAlcool = distancia / mediaAlcool
	consumoGasolina = distancia / mediaGasolina

	gastoAlcool = consumoAlcool * precoAlcool
	gastoGasolina = consumoGasolina * precoGasolina

	fmt.Println("Abastecer com alcool: ", gastoAlcool)
	fmt.Println("Abastecer com gasolina: ", gastoGasolina)

	if gastoAlcool < gastoGasolina {
		fmt.Println("É melhor abastecer com alcool: ", gastoAlcool)
	} else {
		fmt.Println("É melhor abastecer com gasolina: ", gastoGasolina)
	}
}

	