
public class VetorIterador {
    public static void main(String[] args) {
        Conta vetor[] = new Conta[5];
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = new Conta();
            vetor[i].numero = "C" + ((i + 1)*100+500);
            vetor[i].titular = "Nome" + i;
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(vetor[i] + " | ");
        }
        System.out.println();
        for (Conta conteudo : vetor) {
            System.out.print(conteudo + " | ");
        }
        System.out.println();
    }
}
