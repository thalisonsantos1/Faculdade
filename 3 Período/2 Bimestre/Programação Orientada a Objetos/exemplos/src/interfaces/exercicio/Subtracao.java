package exercicio;

public class Subtracao implements OperacaoMatematica {

    private double num1;
    private double num2;
    

    public double calcular(double num1, double num2) {
        return num1 - num2;
    }


    public double getNum1() {
        return num1;
    }


    public void setNum1(double num1) {
        this.num1 = num1;
    }


    public double getNum2() {
        return num2;
    }


    public void setNum2(double num2) {
        this.num2 = num2;
    }

    

    
}
