package heranca.exemplo1;

public class Main {
    public static void main(String[] args) {
        Aluno a = new Aluno();
        a.setNota(90.0);
        a.setNome("Joaquim");
        a.setCpf("44196283837");

// crie uma classe professor que herda de Pessoa e tem como atributo adicional o valor de salário

        Professor p = new Professor();
        p.setSalario(1000.0);
        p.setNome("João");
        p.setCpf("09268076683");
        p.setIdade(35);
    }
}
