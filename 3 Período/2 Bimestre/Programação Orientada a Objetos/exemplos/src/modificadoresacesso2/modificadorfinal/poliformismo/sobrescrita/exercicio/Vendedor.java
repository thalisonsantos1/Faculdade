// Crie uma classe vendedor que herda da classe funcionario e tem atributos valorVendido e percentual de comissão.
// Faça sobrescrita do método getSalarioTotal de maneira que some ao valor de salário e vale alimentação, o valor de sua comissão baseado no valor vendido e o percentual de comissão.

package exercicio;

public class Vendedor extends Funcionario {
    
    private double valorVendido;
    private double percentualComissao;

    public double getValorVendido() {
        return valorVendido;
    }
    public void setValorVendido(double valorVendido) {
        this.valorVendido = valorVendido;
    }
    public double getPercentualComissao() {
        return percentualComissao;
    }
    public void setPercentualComissao(double percentualComissao) {
        this.percentualComissao = percentualComissao;
    }

    public double getSalarioTotal() {
        return super.getSalario() + getValeAlimentacao() + (valorVendido * percentualComissao);
    }
    


}
