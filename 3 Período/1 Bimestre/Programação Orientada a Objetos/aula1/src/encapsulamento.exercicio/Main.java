//package encapsulamento.exercicio;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Funcionario f = new Funcionario();
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o nome do funcionário:");
        f.setNome(sc.nextLine());
        System.out.println("Digite o cargo do funcionário:");
        f.setCargo(sc.nextLine());
        System.out.println("Digite o salário do funcionário:");
        f.setSalario(Double.parseDouble(sc.nextLine()));
        System.out.println("Digite o valor vendido pelo funcionário:");
        f.setValorvendido(Double.parseDouble(sc.nextLine()));
        System.out.println("Digite o percentual de comissão do funcionário:");
        f.setPercentualcomissao(Double.parseDouble(sc.nextLine()));

        System.out.println("Nome: " + f.getNome());
        System.out.println("Cargo: " + f.getCargo());
        System.out.println("Salário: " + f.getSalario());   
        System.out.println("Valor vendido: " + f.getValorvendido());
        System.out.println("Percentual de comissão: " + f.getPercentualcomissao());
        System.out.println("Comissão: " + f.calcularComissao());
        System.out.println("Salário total: " + f.calcularSalario());
    }
}
