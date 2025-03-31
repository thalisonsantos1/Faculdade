/*7.	Implemente um programa que rotacione os elementos do array k posições para a direita. Exemplo:
Entrada: [1, 2, 3, 4, 5], k = 2  
Saída: [4, 5, 1, 2, 3] */


package exercicio07;

public class exercicio07 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int k = 2;
        int n = array.length;

        // Imprime o array original
        System.out.print("Array original: ");
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // Rotaciona o array k posições para a direita
        rotateArray(array, k, n);
        
        // Imprime o array rotacionado
        for (int i : array) {
            System.out.print(i + " ");
        }
    }

    public static void rotateArray(int[] array, int k, int n) {
        // Se k for maior que n, ajusta k para evitar rotações desnecessárias
        k = k % n;
        
        // Inverte o array inteiro
        reverse(array, 0, n - 1);
        
        // Inverte os primeiros k elementos
        reverse(array, 0, k - 1);
        
        // Inverte os últimos n-k elementos
        reverse(array, k, n - 1);
    }

    public static void reverse(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }

}
