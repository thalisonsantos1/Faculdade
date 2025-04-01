import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // criando a cidade

        Cidade patolandia = new Cidade();
        patolandia.setNome("Patolândia");
        patolandia.setEstado("MG");

        // criando o endereço
        Endereco endereco = new Endereco();
        endereco.setLogradouro("Rua Pimenta de Padua");
        endereco.setNumero("350");
        endereco.setBairro("Centro");
        endereco.setCidade(patolandia);

        // criando as crianças
        Crianca zezinho = new Crianca();
        zezinho.setNome("Zezinho da Silva");
        zezinho.setIdade(8);

        Crianca luizinho = new Crianca();
        luizinho.setNome("Luizinho da Silva");
        luizinho.setIdade(10);

        Crianca huguinho = new Crianca();
        huguinho.setNome("Huguinho da Silva");
        huguinho.setIdade(9);

        Crianca patolino = new Crianca();
        patolino.setNome("Patolino da Silva");
        patolino.setIdade(11);

        // criando os responsáveis

        Responsavel donald = new Responsavel();
        donald.setNome("Donald");
        donald.setCpf("111.111.111-11");
        donald.setTelefone("(11) 1111-1111");
        donald.setEmail("donald@patolandia.com");
        donald.setEndereco(endereco);
        donald.addCrianca(zezinho);
        donald.addCrianca(luizinho);
        zezinho.getResponsaveis().add(donald);
        luizinho.getResponsaveis().add(donald);

        Responsavel patinhas = new Responsavel();
        patinhas.setNome("Patinhas");
        patinhas.setCpf("222.222.222-22");
        patinhas.setTelefone("(22) 2222-2222");
        patinhas.setEmail("patinhas@patolandia.com");
        patinhas.setEndereco(endereco);
        patinhas.addCrianca(zezinho);
        patinhas.addCrianca(huguinho);
        patinhas.addCrianca(patolino);
        zezinho.getResponsaveis().add(patinhas);
        huguinho.getResponsaveis().add(patinhas);
        patolino.getResponsaveis().add(patinhas);

        Responsavel margarida = new Responsavel();
        margarida.setNome("Margarida");
        margarida.setCpf("333.333.333-33");
        margarida.setTelefone("(33) 3333-3333");
        margarida.setEmail("margarida@patolandia.com");
        margarida.setEndereco(endereco);
        margarida.addCrianca(zezinho);
        zezinho.getResponsaveis().add(margarida);

        // adicionando os responsáveis ao endereço
        endereco.setResponsavel(patinhas);

        // adicionando o endereço à cidade

        patolandia.addEnderecos(endereco);

        // imprimindo os dados
        System.out.println("------ Dados da Cidade ------");
        System.out.println("Cidade : " + patolandia.getNome() + " - " + patolandia.getEstado());
        System.out.println("\n------ Endereço ------");
        System.out.println("Logradouro: " + endereco.getLogradouro() + ", " + endereco.getNumero());
        System.out.println("Bairro: " + endereco.getBairro());
        System.out.println("Cidade: " + endereco.getCidade().getNome() + " - " + endereco.getCidade().getEstado());

        System.out.println("---- Responsáveis e Crianças ----");
        List<Responsavel> responsaveis = new ArrayList<>();
        responsaveis.add(donald);
        responsaveis.add(patinhas);
        responsaveis.add(margarida);

        for (Responsavel responsavel : responsaveis) {
            System.out.println("\nResponsável: " + responsavel.getNome());
            System.out.println("CPF: " + responsavel.getCpf());
            System.out.println("Telefone: " + responsavel.getTelefone());
            System.out.println("Email: " + responsavel.getEmail());
            System.out.println("Crianças sob responsabilidade: ");

            for (Crianca crianca : responsavel.getCriancas()) {
                System.out.println("- " + crianca.getNome() + " (" + crianca.getIdade() + " anos)");
            }
            
        }

    }

}
 