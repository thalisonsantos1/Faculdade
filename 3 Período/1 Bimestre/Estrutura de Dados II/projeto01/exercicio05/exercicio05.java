package exercicio05;

public class exercicio05 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int numero = 0;
        boolean encontrado = false;
        int i = 0;
        
        for (i = 0; i < numeros.length; i++) {
            numeros[i] = (int) (Math.random() * 101);
        }
        
        System.out.print("Digite um número: ");
        numero = Integer.parseInt(System.console().readLine());
        
        for (i = 0; i < numeros.length; i++) {
            if (numeros[i] == numero) {
                encontrado = true;
                break;
            }
        }
        if (encontrado) {
            System.out.println("Número encontrado na posição: " + i);
        } else {
            System.out.println("Número não encontrado.");
        }
    }
}
