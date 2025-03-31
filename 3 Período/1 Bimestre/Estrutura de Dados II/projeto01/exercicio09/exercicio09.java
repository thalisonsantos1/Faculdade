package exercicio09;

public class exercicio09 {
    public static void main(String[] args) {
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int SomaMax = findMaxSubArraySum(arr);
        System.out.println("A maior soma do subarray é: " + SomaMax);
    }

    public static int findMaxSubArraySum(int[] arr) {
        int SomaMax = arr[0], somaAtual = arr[0];
        for (int i = 1; i < arr.length; i++) {
            somaAtual = Math.max(arr[i], somaAtual + arr[i]);
            SomaMax = Math.max(SomaMax, somaAtual);
        }
        return SomaMax;
    }

}
