import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;

public class App {
    public static int funcaoHash (String palavra, int tam) {
        int hash = 0;
        //hash = 13 + palavra.toUpperCase().charAt(0);
        palavra = palavra.toUpperCase();
        for (int i = 0; i < palavra.length(); i++) {
            hash += palavra.charAt(i); // ao inves de pegar a inicial, ele soma todos os numeros da tabela ascii
        }
        return hash % tam;       
    }
    public static boolean buscarPalavra(String palavra, ArrayList<String>[] tabelaHash, int tam) {
        int categoria = funcaoHash(palavra, tam);
        ArrayList<String> elementos = tabelaHash[categoria];
        return  elementos.contains(palavra.toUpperCase());
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
        List<String> listaPalavras = GeradorPalavras.lerPalavras();
        for (String palavra : listaPalavras) {
            palavra = palavra.toUpperCase();
            int categoria = funcaoHash(palavra, totalCategorias);
            tabelaHash[categoria].add(palavra);
        }

        System.out.println("__Preenchida___");
        for (int i = 0; i<tabelaHash.length; i++) {
            ArrayList <String> el =  tabelaHash[i];

            String letra = el.get(0);
            System.out.println(i + "-> " + letra + "-> " + el.size());

        }
        int opcao = 0;
        do{
            String procurar = JOptionPane.showInputDialog("Digite: ");
            boolean result = buscarPalavra(procurar, tabelaHash, totalCategorias);
            if(result){
                JOptionPane.showMessageDialog(null, "Achei" + procurar);
            }else{
                JOptionPane.showMessageDialog(null, "Nao achei" + procurar);
            }
            opcao = JOptionPane.showConfirmDialog(null, "Deseja continuar?");
        } while (opcao == JOptionPane.YES_OPTION);
    }

}    
    
