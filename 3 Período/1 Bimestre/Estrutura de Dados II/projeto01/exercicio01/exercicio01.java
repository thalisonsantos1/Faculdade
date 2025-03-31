package exercicio01;

public class exercicio01 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int maior = 0;
        int menor = 0;
        System.out.println("Crie um conjunto com 10 números inteiros.");
        System.out.println("Digite os números: ");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = Integer.parseInt(System.console().readLine());
            if (i == 0) {
                maior = numeros[i];
                menor = numeros[i];
            } else {
                if (numeros[i] > maior) {
                    maior = numeros[i];
                }
                if (numeros[i] < menor) {
                    menor = numeros[i];
                }
            }
        }
        System.out.println("Maior: " + maior);
        System.out.println("Menor: " + menor);
    }
}
