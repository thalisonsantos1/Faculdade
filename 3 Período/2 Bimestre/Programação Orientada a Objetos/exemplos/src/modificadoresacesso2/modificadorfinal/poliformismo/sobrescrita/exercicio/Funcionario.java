// Crie uma classe funcionario contendo o nome, cpf, salario e vale alimentação
// Crie um metodo getSalarioTotal que retorne a soma do seu salário com o vale alimentação
// Crie uma classe vendedor que herda da classe funcionario e tem atributos valorVendido e percentual de comissão.
// Faça sobrescrita do método getSalarioTotal de maneira que some ao valor de salário e vale alimentação, o valor de sua comissão baseado no valor vendido e o percentual de comissão.
// Crie uma classe horista que herda da classe funcionario e tem o atributo horastrabalhadas. 
// Faça sobrescrita do método getSalarioTotal de maneira que o calculo do seu salario de acordo com as horas trabalhadas, sendo que o valor do salario é com base em 160 horas mensais e deve-se calcular o salario proporcional para depois somar com o vale alimentação.



package exercicio;

public class Funcionario {

    private String nome;
    private String cpf;
    private double salario;
    private double valeAlimentacao;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }
    public double getValeAlimentacao() {
        return valeAlimentacao;
    }
    public void setValeAlimentacao(double valeAlimentacao) {
        this.valeAlimentacao = valeAlimentacao;
    }

    public double getSalarioTotal() {
        return salario + valeAlimentacao;
    }

}
