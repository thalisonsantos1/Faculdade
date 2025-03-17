package Construtores.exercicio1;

public class Pessoa {
    String nome;
    int idade;

    public Pessoa(){
        System.out.println("Construtor sem parâmetros");
    }
    public Pessoa(String novoNome){
        nome = novoNome;
        System.out.println("SEja bem vindo " + nome);
    }
    public Pessoa(String novoNome, int novaIdade){
        nome = novoNome;
        idade = novaIdade;
        System.out.println("Seja bem vindo " + nome + " com " + idade + " anos");
    }

}
