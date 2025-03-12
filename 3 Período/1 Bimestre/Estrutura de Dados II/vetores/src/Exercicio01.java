
import javax.swing.JOptionPane;

public class Exercicio01 {
    public static String imprimir(int [] v) {
        String saida = "[";
        for (int i = 0; i < v.length; i++) {
            saida = saida + v[i] + " ";
        }
        saida += "]";
        JOptionPane.showMessageDialog(null, saida);
        return saida;
    }

    public static void main(String[] args) {
        /*Criar um programa que receba um array (vetor) de N numeros inteiros e calcule a soma de todos os elementos */

        int totalNumeros = 0;
        // entrada de dados usando JOptionPane (janela de dialogo)
        String totalNumerosStr = JOptionPane.showInputDialog("Tamanho do vetor: ");
        //altera o tipo de dados da variavel totalNumerosStr de String para int
        totalNumeros = Integer.parseInt(totalNumerosStr);
        //criar vetor
        int[] numeros = new int[totalNumeros];
        imprimir(numeros);
        //preencher o vetor
        for (int i = 0; i < numeros.length; i++) {
            String aux = JOptionPane.showInputDialog("Digite:  ");
            numeros[i] = Integer.valueOf(aux);
        }
        String s = imprimir(numeros);     

        // somar todos os elementos do vetor
        int soma = 0;
        for (int i = 0; i < numeros.length; i++) {
            soma += numeros[i];
        }
        JOptionPane.showMessageDialog(null, "vetor: " + s + "\nSoma: " + soma);
    }
    

}
