
import java.util.*;
import model.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MapaCidades mapa = new MapaCidades();

        int opcao;
        do { 
            System.out.println("\n---MENU DO SISTEMA DE CIDADES---\n");
            System.out.println("1 - Cadastrar cidade");
            System.out.println("2 - Conectar cidades");
            System.out.println("3 - Listar conexões de uma cidade");
            System.out.println("4 - Verificar se duas cidades estao conectadas");
            System.out.println("5 - Listar cidades sem conexao");
            System.out.println("6 - Mostrar a cidade mais populosa");
            System.out.println("7 - Sair\n");

            System.out.print("Digite a opção desejada: ");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o nome da cidade: ");
                    String nome = scanner.nextLine();

                    System.out.print("Digite a sigla da UF: ");
                    String estado = scanner.nextLine();

                    System.out.print("Informe o número de habitantes da cidade: ");
                    int populacao = scanner.nextInt();                    
                    scanner.nextLine();

                    Cidade novaCidade = new Cidade(nome, estado, populacao);
                    mapa.adicionarCidade(novaCidade);
                    System.out.println("Cidade cadastrada com sucesso!");

                    break;

                case 2:
                    System.out.print("Digite o nome da cidade de origem: ");
                    String origem = scanner.nextLine();

                    System.out.print("Digite o nome da cidade de destino: ");
                    String destino = scanner.nextLine();

                    System.out.print("Digite a distância em km: ");
                    int distancia = scanner.nextInt();
                    scanner.nextLine();

                    Cidade cidadeOrigem  = mapa.buscarCidadePorNome(origem);
                    Cidade cidadeDestino = mapa.buscarCidadePorNome(destino);

                    if (cidadeOrigem != null && cidadeDestino != null) {
                        mapa.conectarCidades(cidadeOrigem, cidadeDestino, distancia);
                        System.out.println("Conexao realizada com sucesso!");
                    } else {
                        System.out.println("Uma ou mais cidades não foram encontradas");
                    }
                    break;

                case 3:
                    System.out.print("Digite o nome da cidade: ");
                    String nomeCidade = scanner.nextLine();

                    Cidade cidade = mapa.buscarCidadePorNome(nomeCidade);
                    if (cidade != null) {
                        mapa.listarConexoes(cidade);
                    } else {
                        System.out.println("Cidade não encontrada.");
                    }
                    break;

                case 4:
                    System.out.print("Digite o nome da cidade de origem: ");
                    String origemCaminho = scanner.nextLine();

                    System.out.print("Digite o nome da cidade de destino: ");
                    String destinoCaminho = scanner.nextLine();

                    Cidade origemBusca = mapa.buscarCidadePorNome(origemCaminho);
                    Cidade destinoBusca = mapa.buscarCidadePorNome(destinoCaminho);
                    
                     if (origemBusca != null && destinoBusca != null) {
                        boolean conectadas = mapa.existeCaminho(origemBusca, destinoBusca);
                        System.out.println("Existe caminho? " + (conectadas ? "Sim" : "Nao"));
                    } else {
                        System.out.println("Uma ou mais cidades nao foram encontradas");
                    }
                    break;

                case 5:
                    System.out.println("Cidades sem conexao: ");
                    mapa.listarCidadesSemConexao();
                    break;

                case 6:
                    Cidade cidadeMaisPopulosa = mapa.buscarCidadeMaisPopulosa();
                    System.out.println("Cidade mais populosa: " + cidadeMaisPopulosa.getNome());
                    break;

                case 7:
                    System.out.println("Saindo do sistema...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        } while (opcao != 6);

        scanner.close();
    }
}
