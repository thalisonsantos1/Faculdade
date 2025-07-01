

import model.Cidade;
import model.MapaCidades;

public class Main {
    public static void main(String[] args) {
        MapaCidades mapa = new MapaCidades();

        Cidade c1 = new Cidade("São Sebastião do Paraíso", "MG", 70000);
        Cidade c2 = new Cidade("Itamogi", "MG", 10700);
        Cidade c3 = new Cidade("Monte Santo de Minas", "MG", 20800);
        Cidade c4 = new Cidade("São Tomás de Aquino", 6740);
        Cidade c5 = new Cidade("Carrancas", "MG", 5000);

        mapa.adicionarCidade(c1);
        mapa.adicionarCidade(c2);
        mapa.adicionarCidade(c3);
        mapa.adicionarCidade(c4);
        mapa.adicionarCidade(c5);

        mapa.conectarCidades(c1, c2, 30);
        mapa.conectarCidades(c2, c3, 20);
        mapa.conectarCidades(c1, c4, 15);
        // c5 ficará sem conexão

        mapa.listarConexoes(c1);
        mapa.listarConexoes(c3);

        System.out.println("\nExiste caminho entre Paraíso e São Tomás de Aquino? " +
                mapa.existeCaminho(c1, c4));

        System.out.println("Existe caminho entre Paraíso e Carrancas? " +
                mapa.existeCaminho(c1, c5));

        System.out.println("\nCidades sem conexão:");
        mapa.listarCidadesSemConexao();
    }
}

/* IMPLEMENTAR: 
Funcionalidades

Cadastro de Cidades
Cada cidade deve conter:
Nome
Estado (UF)
População
As cidades devem ser armazenadas de forma ordenada por nome ou população utilizando TreeSet.
Criação de Rotas (Conexões entre cidades)
Cada rota deve indicar a cidade de destino e a distância (em km).
Usar um grafo não direcionado implementado com HashMap<Cidade, Set<Rota>>.
Consultas no Sistema
Mostrar todas as conexões (rotas) de uma cidade.
Verificar se duas cidades estão conectadas.
Listar todas as cidades sem nenhuma conexão.

 * 
 * 
 */
