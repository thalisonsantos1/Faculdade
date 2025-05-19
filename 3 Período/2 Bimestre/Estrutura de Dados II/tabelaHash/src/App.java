
import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;

public class App {
    public static int funcaoHash (String palavra, int tam) {
        int hash = 0;
        // ex: Abobora -> pega letra A -> int da tabela ASCII
        // A -> valor 65
        // 65 -> 0
        // 90 -> 25

        //hash = 13 + palavra.toUpperCase().charAt(0); //pega a primeira letra da palavra
        
        palavra.toUpperCase();
        for (int i = 0; i < palavra.length(); i++) {
            hash += palavra.charAt(i); 
        }
        return hash % tam;       
    }

    public static boolean buscarPalavra (String palavra, ArrayList<String> tabelaHash[], int tam) {
        if (palavra == null || palavra.isEmpty()) {
            return false;
        }
        
        int categoria = funcaoHash(palavra, tam);
        if (tabelaHash[categoria] != null && tabelaHash[categoria].contains(palavra)) {
            return true;
        }
        
        return false;
    }    

    public static void main(String[] args) throws Exception {
        int totalCategorias = 10;
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
        List<String> listaPalavra = GeradorPalavras.lerPalavras();
        for (String palavra : listaPalavra) {
            palavra = palavra.toUpperCase();
            int categoria = funcaoHash(palavra, totalCategorias);
            tabelaHash[categoria].add(palavra);
        }

        //for (int i = 0; i < 100; i++) {
        //    String palavra  = GeradorPalavras.gerarPalavraAleatoria(3, 10);
        //    int categoria = funcaoHash(palavra, totalCategorias);
        //    tabelaHash[categoria].add(palavra);
        //}
        System.out.println("PREENCHIDA");
        for (int i = 0; i < tabelaHash.length; i++) {
            ArrayList<String> el = tabelaHash[i];
            String letra = el.get(0);
            System.out.println(i + "-> " + letra + " -> " + el.size());
        }

        int opcao = 0;
        do {
            String procurar = JOptionPane.showInputDialog("Digite a palavra que deseja buscar: ");
            boolean resultado = buscarPalavra(procurar, tabelaHash, totalCategorias);
            if (resultado) {
                JOptionPane.showMessageDialog(null, "Palavra encontrada na categoria: " + funcaoHash(procurar, totalCategorias));
            } else {
                JOptionPane.showMessageDialog(null, "Palavra nao encontrada");
            }
            opcao = JOptionPane.showConfirmDialog(null, "Deseja procurar outra palavra?");
        } while (opcao == JOptionPane.YES_OPTION);

        // teste de desempenho

        long inicio  = System.currentTimeMillis();
        for (String palavra : listaPalavra) {
           listaPalavra.contains(palavra);
        }
        long fim = System.currentTimeMillis();
        System.out.println("Tempo de execucao: " + (fim - inicio) + "ms");

        

        inicio  = System.currentTimeMillis();
        for (String palavra : listaPalavra) {
           buscarPalavra(palavra, tabelaHash, totalCategorias);
        }
        fim = System.currentTimeMillis();
        System.out.println("Tempo de execucao: " + (fim - inicio) + "ms");
        



        /*System.out.println("*******Buscando palavra********");

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite a palavra que deseja buscar: ");
        String palavraBusca = sc.nextLine();

        

        if (buscarPalavra(palavraBusca, tabelaHash, totalCategorias)){
            System.out.println("Palavra encontrada na categoria: " + funcaoHash(palavraBusca, totalCategorias));
        } else {
            System.out.println("Palavra nao encontrada");
        }

        sc.close();

    }*/
    }
}

