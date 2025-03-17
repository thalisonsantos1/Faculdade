package Construtores.exercicio1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();

        Pessoa p2 = new Pessoa("João");

        Pessoa p3 = new Pessoa("Maria", 25);

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o nome da pessoa: ");
        Pessoa p4 = new Pessoa(sc.nextLine());

        System.out.println("Digite o nome e a idade: ");
        Pessoa p5 = new Pessoa(sc.nextLine(), Integer.parseInt(sc.nextLine()));
    }

}