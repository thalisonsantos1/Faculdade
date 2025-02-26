
import java.util.Scanner;

public class correcaoex1 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner in = new Scanner(System.in);
        double soma = 0;
        for (int i = 0; i < 3; i++) {
            System.out.println("Digite a nota " + (i + 1) + ": ");
            double nota = in.nextDouble();
            soma += nota;
            }
        double media = soma / 3;
        if (media >= 7){
        System.out.println("Aprovado com Media= " + media);
        }else{
            double falta = 7 - media;
            System.out.println("Reprovado, precisando de = " + falta + " pontos para a aprovação");
        }
    }
}
