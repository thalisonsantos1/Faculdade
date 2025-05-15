package exercicio;

public class Main {

    public static void main(String[] args) {

        Horista h = new Horista();
        h.setSalario(2000);
        h.setHorasTrabalhadas(100);
        h.setValeAlimentacao(100);
        System.out.println("Salario total Horista: " + h.getSalarioTotal());

        Vendedor v = new Vendedor();
        v.setSalario(2000);
        v.setValorVendido(2000);
        v.setPercentualComissao(0.05);
        v.setValeAlimentacao(100);
        System.out.println("Salario total Vendedor: " + v.getSalarioTotal());

    }


}
