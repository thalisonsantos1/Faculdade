package model;
import java.util.*;

public class MapaCidades {
    private Set<Cidade> cidades; // TreeSet para manter as cidades em ordem alfabética
    private Map<Cidade, Set<Rota>> grafo; // grafo não direcionado

    public MapaCidades() {
        cidades = new TreeSet<>(); 
        grafo = new HashMap<>(); 
    }

    public void adicionarCidade(Cidade cidade) {
        cidades.add(cidade);
        grafo.put(cidade, new HashSet<>());
    }

    public void conectarCidades(Cidade origem, Cidade destino, int distancia) {
        if (!cidades.contains(origem) || !cidades.contains(destino)) {
            System.out.println("Uma ou ambas as cidades não estão cadastradas no mapa.");
            return;
        }
        
        grafo.get(origem).add(new Rota(destino, distancia));
        grafo.get(destino).add(new Rota(origem, distancia));
    }

    public void listarConexoes(Cidade cidade){
        Set<Rota> rotas = grafo.get(cidade);
        System.out.println("\nConexões de " + cidade.getNome() + ":");

        if (rotas == null || rotas.isEmpty()) {
            System.out.println("Nenhuma rota encontrada para essa cidade.");
        } else {
            for (Rota rota : rotas) {
                System.out.println("  " + rota);
            }
        }
    }

    public boolean existeCaminho(Cidade origem, Cidade destino) {
        Set<Cidade> visitados = new HashSet<>();
        return buscaProfundidade(origem, destino, visitados);
    }

    private boolean buscaProfundidade(Cidade atual, Cidade destino, Set<Cidade> visitados) {
        if (atual.equals(destino)) return true;

        visitados.add(atual);

        for (Rota rota : grafo.getOrDefault(atual, Collections.emptySet())) {
            Cidade vizinha = rota.getDestino();
            if (!visitados.contains(vizinha)) {
                if (buscaProfundidade(vizinha, destino, visitados)){
                    return true;
                }
            }
        }
        return false;
    }

    public void listarCidadesSemConexao() {
        for (Cidade cidade : cidades) {
            Set<Rota> rotas = grafo.getOrDefault(cidade, Collections.emptySet()); // Obtenha as rotas da cidade (ou um conjunto vazio, defaultValue)
            if (rotas.isEmpty()) {
                System.out.println("Cidade sem conexão: " + cidade.getNome());
            }
        }
    }

    public Cidade buscarCidadePorNome(String nome) {
        for (Cidade cidade : cidades) {
            if (cidade.getNome().equalsIgnoreCase(nome)) {
                return cidade;
            }
        }
        return null;
    }

    public Cidade buscarCidadeMaisPopulosa() {
        Cidade cidadeMaisPopulosa = null;
        int maiorPopulacao = 0;

        for (Cidade cidade : cidades) {
            if (cidade.getPopulacao() > maiorPopulacao) {
                cidadeMaisPopulosa = cidade;
                maiorPopulacao = cidade.getPopulacao();
            }
        }
        return cidadeMaisPopulosa;
    }

    public Set<Cidade> getCidades() {
        return cidades;
    }

    public void setCidades(Set<Cidade> cidades) {
        this.cidades = cidades;
    }

    

}
