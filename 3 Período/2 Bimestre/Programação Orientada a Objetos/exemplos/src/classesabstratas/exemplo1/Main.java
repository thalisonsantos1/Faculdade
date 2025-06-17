package classesabstratas.exemplo1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Carro c = new Carro();
        Barco b = new Barco();
        Aviao a = new Aviao();

        c.setModelo("Fusca");
        c.setMarca("Volkswagen");
        c.setPlaca("MIQ-4C40");        
        Scanner valorC = new Scanner(System.in);
        System.out.println("Digite o valor do carro: ");
        c.setValorDoVeiculo(valorC.nextDouble());        
        System.out.println(c.getModelo() + " " + c.getNomeImposto() + ": " + c.getValorImposto(c.getValorDoVeiculo()));


        b.setModelo("Ipanema");
        b.setMarca("Ferrovial");
        b.setNumerRegistro(1234567);
        Scanner valorB = new Scanner(System.in);
        System.out.println("Digite o valor do barco: ");
        c.setValorDoVeiculo(valorB.nextDouble());        
        System.out.println(b.getModelo() + " " + b.getNomeImposto() + ": " + b.getValorImposto(b.getValorDoVeiculo()));


        a.setModelo("Boing 747");
        a.setMarca("Boing");
        a.setNumeroAnac(1234567);
        Scanner valorA = new Scanner(System.in);
        System.out.println("Digite o valor do aviao: ");
        a.setValorDoVeiculo(valorA.nextDouble());

        
        System.out.println(a.getModelo() + " " + a.getNomeImposto() + ": " + a.getValorImposto(a.getValorDoVeiculo()));


        //Declare um método abstrato double getValorImposto(double valorDoVeiculo) e implemente nas classes filhas;
        //Para Carro, calcule 4% de imposto IPVA sobre o valor do veículo recebido por parametro;
        //Para Barco, calcule 8% de imposto portuário sobre o valor do veículo recebido por parametro;
        //Para Aviao, calcule 12% de imposto ANAC sobre o valor do veículo recebido por parametro;


        
    }
}
