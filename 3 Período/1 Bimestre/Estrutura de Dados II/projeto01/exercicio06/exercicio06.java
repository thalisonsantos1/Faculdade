package exercicio06;

public class exercicio06 {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5};
        int[] numerosSemRepeticao = new int[numeros.length];
        int j = 0;
        for (int i = 0; i < numeros.length; i++) {
            boolean repetido = false;
            for (int k = 0; k < j; k++) {
                if (numeros[i] == numerosSemRepeticao[k]) {
                    repetido = true;
                    break;
                }
            }
            if (!repetido) {
                numerosSemRepeticao[j] = numeros[i];
                j++;
            }
        }
        System.out.println("Array original: ");
        
        for (int i = 0; i < numeros.length; i++) {
            System.out.print(numeros[i] + " ");
        }
        System.out.println("\nArray sem repetições: ");
        
        for (int i = 0; i < j; i++) {
            System.out.print(numerosSemRepeticao[i] + " ");
        }
    }

}
