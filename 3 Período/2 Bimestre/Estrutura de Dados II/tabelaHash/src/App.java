
import java.util.ArrayList;

public class App {
    public static int funcaoHash (String palavra, int tam) {
        int hash = 0;
        // ex: Abobora -> pega letra A -> int da tabela ASCII
        // A -> valor 65
        // 65 -> 0
        // 90 -> 25

        hash = 13 + palavra.toUpperCase().charAt(0);
        return hash % tam;       
    }

    public static void main(String[] args) throws Exception {
        int totalCategorias = 26;
        ArrayList<String> tabelaHash[] = new ArrayList[totalCategorias];
        // inicializando a tabela
        for (int i = 0; i < tabelaHash.length; i++) {
            System.out.println(i + "-> " + tabelaHash[i]);
            tabelaHash[i] = new ArrayList<String>();
        }
        System.out.println("-------------------------------------------");
        for (int i = 0; i < tabelaHash.length; i++) {
            System.out.println(i + "-> " + tabelaHash[i]);
        }

        System.out.println("Adicionando palavras na tabela");
        for (int i = 0; i < 100; i++) {
            String palavra  = GeradorPalavras.gerarPalavraAleatoria(3, 10);
            int categoria = funcaoHash(palavra, totalCategorias);
            tabelaHash[categoria].add(palavra);
        }
        System.out.println("PREENCHIDA");
        for (int i = 0; i < tabelaHash.length; i++) {
            System.out.println(i + "-> " + tabelaHash[i]);
        }

    }
}

