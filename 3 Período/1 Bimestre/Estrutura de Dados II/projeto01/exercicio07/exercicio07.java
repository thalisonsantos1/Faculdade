package exercicio07;

public class exercicio07 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int k = 2;
        int n = array.length;

        
        System.out.print("Array original: ");
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        
        rotateArray(array, k, n);
        
        
        for (int i : array) {
            System.out.print(i + " ");
        }
    }

    public static void rotateArray(int[] array, int k, int n) {
        
        k = k % n;
        
        
        reverse(array, 0, n - 1);
        
        
        reverse(array, 0, k - 1);
        
        
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
