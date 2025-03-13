package Construtores.exercicio2;

public class Retangulo {
    double lado;
    double altura;

    public Retangulo() {
    }

    public Retangulo(double l) {
        lado = l;
    }

    public Retangulo(double l, double a) {
        lado = l;
        altura = a;
    }

    double calcularArea() {
        return lado * altura;
    }

    

}
