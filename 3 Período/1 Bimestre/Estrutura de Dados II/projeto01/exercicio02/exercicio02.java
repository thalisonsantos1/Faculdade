package exercicio02;

public class exercicio02 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int soma = 0, media = 0;
        System.out.println("Crie um conjunto com 10 números inteiros.");
        System.out.println("Digite os números: ");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = Integer.parseInt(System.console().readLine());
            soma += numeros[i];
        }
        media = soma / numeros.length;
        System.out.println("Média: " + media);
    }
}
