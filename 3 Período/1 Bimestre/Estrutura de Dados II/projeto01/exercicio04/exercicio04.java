//4.	Crie um programa que inverta a ordem dos elementos de um array sem usar uma nova estrutura de dados auxiliar.

package exercicio04;

public class exercicio04 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        System.out.println("Crie um conjunto com 10 números inteiros");
        System.out.println("Digite os números:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = Integer.parseInt(System.console().readLine());
        }
        for (int i = 0; i < numeros.length / 2; i++) {
            int temp = numeros[i];
            numeros[i] = numeros[numeros.length - 1 - i];
            numeros[numeros.length - 1 - i] = temp;
        }
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Números: " + numeros[i]);
        }
    }
}
