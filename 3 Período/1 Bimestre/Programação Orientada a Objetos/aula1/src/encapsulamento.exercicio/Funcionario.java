/*Crie uma classe chamada funcionario contendo os atributos encapsulados:
 * nome
 * cargo
 * salario
 * valorvendido
 * percentual de comissao
 O salário não poderá ser menor do que meio salário mínimo (550,00)
 O percentual de comissão não poderá ser negativo e nem maior que 25%.
 O valor vendido não poderá ser negativo
 Crie ainda, um método capaz de retornar o valor da comissão, calculando-se o percentual da comissao sobre o valor vendido.
 */


package encapsulamento.exercicio;

public class Funcionario {

    private String nome;
    private String cargo;
    private double salario;
    private double valorvendido;
    private double percentualcomissao;

    public Funcionario(String nome, String cargo, double salario, double valorvendido, double percentualcomissao) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
        this.valorvendido = valorvendido;
        this.percentualcomissao = percentualcomissao;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        if (salario < 550) {
            salario = 550;
            System.out.println("Salario alterado para: " + salario);
        }else { 
            this.salario = salario;            
        }              
    }

    public double getValorvendido() {
        return valorvendido;
    }

    public void setValorvendido(double valorvendido) {
        this.valorvendido = valorvendido;
    }

    public double getPercentualcomissao() {
        return percentualcomissao;
    }

    public void setPercentualcomissao(double percentualcomissao) {
        if (percentualcomissao < 0 || percentualcomissao > 25) {
            System.out.println("Percentual de comissão inválido!");
        } else {
            this.percentualcomissao = percentualcomissao;
        }
    }
    
    public double calcularComissao() {
        return (valorvendido * percentualcomissao) / 100;
    } 
    
    public double calcularSalario() {
        return salario + calcularComissao();         

    }
    
    public void imprimir() {
        System.out.println("Nome: " + getNome());
        System.out.println("Cargo: " + getCargo());
        System.out.println("Salario: " + getSalario());
        System.out.println("Valor Vendido: " + getValorvendido());
        System.out.println("Percentual de Comissao: " + getPercentualcomissao());
        System.out.println("Comissao: " + calcularComissao());
        System.out.println("Salario Total: " + calcularSalario());
    }   

}
