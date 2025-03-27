package aula1.src.encapsulamento.exemplo;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Produto p = new Produto();
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite a descrição do produto:");
        p.setDescricao(sc.nextLine());
        System.out.println("Digite o preço do produto:");
        p.setPreco(Double.parseDouble(sc.nextLine()));

        System.out.println("descrição: " + p.getDescricao());
        System.out.println("preço: " + p.getPreco());
    }
}
