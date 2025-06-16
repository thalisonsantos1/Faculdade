public class Main {
    public static void main(String[] args) {
        GerenciadorFeira feira = new GerenciadorFeira();

        feira.CadastrarLivro("Java Básico", "Ana Silva", 2015);
        feira.CadastrarLivro("Algoritmos", "Carlos Souza", 2018);
        feira.CadastrarLivro("Programação Java", "Ana Silva", 2019);

        feira.ListarLivros();
        feira.ListarAutores();
    }
}
