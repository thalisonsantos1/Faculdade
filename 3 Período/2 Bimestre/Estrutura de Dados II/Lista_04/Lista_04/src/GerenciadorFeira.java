
import java.util.TreeMap;
import java.util.TreeSet;

public class GerenciadorFeira {
    private TreeSet<Livro> livros = new TreeSet<>();
    private TreeMap<String, TreeSet<String>> autores = new TreeMap<>(); 

    public void CadastrarLivro(String titulo, String autor, int ano) {
        Livro livro = new Livro(titulo, ano);
        livros.add(livro); 

        if (!autores.containsKey(autor)) {
            autores.put(autor, new TreeSet<>());
        }
        autores.get(autor).add(titulo);
    }

    public void ListarLivros() {
        System.out.println("\nTodos os livros:");
        for (Livro livro : livros) {
            System.out.println(livro);
        }
    }
    
    public void ListarAutores() {
        System.out.println("\nAutores e seus livros:");
        for (String autor : autores.keySet()) {
            System.out.println("Autor: " + autor);
            for (String livro : autores.get(autor)) {
                System.out.println("Livro: " + livro);
            }
        }
    }
}
