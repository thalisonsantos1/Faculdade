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
                        listaNomes();
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
                        System.out.println("Arquivo carregado com sucesso!");
                } else {
                        System.out.println("Erro ao carregar o arquivo! A lista será iniciada vazia.");
                }
        }

        private static void adicionaNome() {
                System.out.println("Digite o nome para adicionar: ");
                String nome = scanner.nextLine().trim();
                if (gerenciador.adicionaNome(nome)) {
                        System.out.println("Nome adicionado com sucesso!");
                }
        }

        private static void listaNomes() {
                ArrayList<String> nomesOrdenados = gerenciador.nomesOrdenados();
                if (nomesOrdenados.isEmpty()) {
                        System.out.println("Lista de nomes vazia!");
                } else {
                        System.out.println("----- Lista de Nomes Ordenados -----");
                        for (int i = 0; i < nomesOrdenados.size(); i++) {
                                System.out.println((i + 1) + " - " + nomesOrdenados.get(i));
                        }
                                
                }
        }

        private static void removerNome() {
                System.out.println("Digite o nome para remover: ");
                String nome = scanner.nextLine().trim();
                if (gerenciador.removeNome(nome)) {
                        System.out.println("Nome removido com sucesso!");
                } else {
                        System.out.println("Nome não encontrado");
                }
        }

        private static void buscarNome() {
                System.out.println("Digite o nome para buscar: ");
                String nome = scanner.nextLine().trim();
                if (gerenciador.buscaNome(nome)) {
                        System.out.println("Nome encontrado!");
                } else {
                        System.out.println("Nome não encontrado");
                }
        }

        private static void salvarDados() {
                boolean sucesso = GerenciadorJson.salvar(gerenciador.getNomes(), arquivo);
                if (sucesso) {
                        System.out.println("Arquivo salvo com sucesso!");
                } else {
                        System.out.println("Erro ao salvar o arquivo!");
                }
        }

        private static void carregarDados() {
                carregarDados();
        }
}
