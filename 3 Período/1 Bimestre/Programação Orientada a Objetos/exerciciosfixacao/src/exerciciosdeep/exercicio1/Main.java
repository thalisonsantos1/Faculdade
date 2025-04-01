package exerciciosdeep.exercicio1;

public class Main {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        p1.nome = "thalison";
        p1.idade = 32;
        p1.cpf = "5412369872";
        p1.validaCpf();
        p1.fazerAniversario();
        p1.apresentar();
    }

}
