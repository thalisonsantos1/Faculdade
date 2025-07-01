package model;

import java.util.Objects;


public class Cidade implements Comparable<Cidade> {
    private String nome;
    private String estado;
    private int populacao;

    public Cidade(String nome, String estado, int populacao) {
        this.nome = nome;
        this.estado = estado;
        this.populacao = populacao;
    }

    public Cidade (String nome, int populacao) {
        this(nome, "", populacao);        
    }

    public String getNome() {
        return nome;
    }

    public String getEstado() {
        return estado;
    }

    public int getPopulacao() {
        return populacao;
    }

    @Override
    public String toString() {
        return nome + (estado.isEmpty() ? "" : ", " + estado) + " (" + populacao + " habitantes)";
    }

    @Override
    public int compareTo(Cidade outra) {
        return this.nome.compareToIgnoreCase(outra.nome);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (!(obj instanceof Cidade)) {
            return false;
        }
        Cidade cidade = (Cidade) obj;
        return nome.equalsIgnoreCase(nome) && estado.equalsIgnoreCase(cidade.estado);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nome.toLowerCase());
    }
}

