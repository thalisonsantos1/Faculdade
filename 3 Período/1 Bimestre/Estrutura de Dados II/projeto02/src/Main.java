import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    private static String arquivo = "nomes.json";
    private static Scanner scanner = new Scanner(System.in);
    private static GerenciadorNomes gerenciador = new GerenciadorNomes();
    private static boolean executando = true;

    public static void main(String[] args) {
        carregaDados();
        while (executando) {
            exibeMenu();
            int opcao = scanner.nextInt();
            scanner.nextLine();
            
            if (opcao == 1) {
                    adicionaNome();
            } else if (opcao == 2) {
                    listarNomes();
            } else if (opcao == 3) {
                    removerNome();
            } else if (opcao == 4) {
                    buscarNome();
            } else if (opcao == 5) {
                    salvarDados();
            } else if (opcao == 6) {
                    carregaDados();
            } else if (opcao == 0) {
                    executando = false;
                    System.out.println("Encerrando o programa...");
            } else {
                    System.out.println("Opção inválida!");
            }
        }
        
    }

    private static void exibeMenu() {
        System.out.println("Escolha uma opção:");
        System.out.println("1 - Adicionar nome");
        System.out.println("2 - Listar nomes");
        System.out.println("3 - Remover nome");
        System.out.println("4 - Buscar nome");
        System.out.println("5 - Salvar Nome no Arquivo");
        System.out.println("6 - Carregar Nome do Arquivo");
        System.out.println("0 - Sair");
        System.out.println("Escolha uma opção: ");
    }

    private static void carregaDados() {
        ArrayList<String> nomesCarregados = GerenciadorJson.carregar(arquivo);
        if (nomesCarregados != null) {
            gerenciador.setNomes(nomesCarregados);
        }
    }

}
