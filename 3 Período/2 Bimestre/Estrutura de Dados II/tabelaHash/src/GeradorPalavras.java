import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GeradorPalavras {

    public static String gerarPalavraAleatoria(int tamanhoMin, int tamanhoMax) {
        Random random = new Random();
        int tamanho = random.nextInt(tamanhoMax - tamanhoMin + 1) + tamanhoMin;
        StringBuilder palavra = new StringBuilder(tamanho);

        for (int i = 0; i < tamanho; i++) {
            // Gera um caractere aleatório entre 'a' (97) e 'z' (122)
            char letra = (char) (random.nextInt(26) + 97);
            palavra.append(letra);
        }

        return palavra.toString();
    }

    public static List <String> lerPalavras(){
        List<String> palavras = new ArrayList<>();
        //tratamento de exceção
        try {
            FileReader arquivo = new FileReader("TabelaHash06\\file\\palavras.txt");
            BufferedReader leitor = new BufferedReader(arquivo);
            String linha;
            while ((linha = leitor.readLine()) != null) {
                //System.out.println(linha);
                palavras.add(linha); //adicionar na estrutura de dados
            }
            System.out.println("Arquivo lido");
        } catch (Exception e) {
            System.out.println("Falha na leitura do arquivo");
        }
        return palavras;
    }


    public static void main(String[] args) {
        lerPalavras();
    }
    
}