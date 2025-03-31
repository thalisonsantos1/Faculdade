//5.	Crie um array de 10 posições com numeros aleatórios entre 0 e 100 através de uma classe ramdom. Peça ao usuário um número e verifique se ele está presente no array criado pelo sistema. Exiba a posição caso esteja.

package exercicio05;

public class exercicio05 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int numero = 0;
        boolean encontrado = false;
        int i = 0;
        // Criando o array com números aleatórios entre 0 e 100
        for (i = 0; i < numeros.length; i++) {
            numeros[i] = (int) (Math.random() * 101);
        }
        // Pega o número do usuário
        System.out.print("Digite um número: ");
        numero = Integer.parseInt(System.console().readLine());
        // Verifica se o número foi encontrado no array
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
