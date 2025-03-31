/*8.	Dado dois arrays ordenados, crie um terceiro array que contenha todos os elementos ordenados.
Entrada: [1, 3, 5] e [2, 4, 6]  
Saída: [1, 2, 3, 4, 5, 6]
*/

package exercicio08;

public class exercicio08 {
    public static void main(String[] args) {
        int[] array1 = {1, 3, 5};
        int[] array2 = {2, 4, 6};
        int n1 = array1.length;
        int n2 = array2.length;
        int[] mergedArray = new int[n1 + n2];

        // Imprime os arrays originais
        System.out.print("Array 1: ");
        for (int i : array1) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        System.out.print("Array 2: ");
        for (int i : array2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Mescla os dois arrays ordenados
        mergeArrays(array1, array2, mergedArray, n1, n2);

        // Imprime o array mesclado
        System.out.print("Array mesclado: ");
        for (int i : mergedArray) {
            System.out.print(i + " ");
        }
    }

    public static void mergeArrays(int[] array1, int[] array2, int[] mergedArray, int n1, int n2) {
        int i = 0, j = 0, k = 0;

        while (i < n1 && j < n2) {
            if (array1[i] < array2[j]) {
                mergedArray[k++] = array1[i++];
            } else {
                mergedArray[k++] = array2[j++];
            }
        }

        while (i < n1) {
            mergedArray[k++] = array1[i++];
        }

        while (j < n2) {
            mergedArray[k++] = array2[j++];
        }
    }

}
