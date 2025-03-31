//Preencha um array com 10 números e conte quantos são pares e quantos são ímpares.

package exercicio03;

public class exercicio03 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int pares = 0; 
        int impares = 0;
        System.out.println("Crie um conjunto com 10 números inteiros.");
        System.out.println("Digite os números: ");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = Integer.parseInt(System.console().readLine());
            if (numeros[i] % 2 == 0) {
                pares += 1;
            } else {
                impares += 1;
            }
        }
        System.out.println("Pares: " + pares);
        System.out.println("Impares: " + impares);
    }
}
