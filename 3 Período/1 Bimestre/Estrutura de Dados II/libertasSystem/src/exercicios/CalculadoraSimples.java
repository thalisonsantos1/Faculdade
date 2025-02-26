package exercicios;

import java.util.Scanner;

/*Crie um programa em Java que peça ao usuário dois números inteiros e uma operação matemática (+, -, * e /)

O programa deve exibir o resultado da operação escolhida.

Requisitos:

- Utilizar Scanner para entrada de dados;
- Utilizar estrutura condicional (if-else ou switch);
- Criar uma classe CalculadoraSimples com um método main. */

public class CalculadoraSimples {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número: ");
        int num1 = scanner.nextInt();
        System.out.println("Digite o segundo número: ");
        int num2 = scanner.nextInt();
        System.out.println("Digite a operação desejada: (+, -, * ou /)");
        String opcao = scanner.next();

        if (opcao.equals("+")) {
            int soma = (num1 + num2);
            System.out.println("o resultado é " + soma);
        }
        if (opcao.equals("-")) {
            int subtracao = (num1 - num2);
            System.out.println("o resultado é " + subtracao);
        }
        if (opcao.equals("*")) {
            int multiplicacao = (num1 * num2);
            System.out.println("o resultado é " + multiplicacao);
        }
        if (opcao.equals("/")) {
            int divisao = (num1 / num2);
            System.out.println("o resultado é " + divisao);
        }
    }

}
