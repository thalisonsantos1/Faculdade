// Crie uma classe Calculadora e faça poliformismo de sobrecarga, ou seja, todos os métodos devem possuir o mesmo nome e ter as seguintes funcionalidades:
// somar 2 numeros inteiros
// somar 2 numeros double
// somar 2 numeros String(fazendo conversão de tipo)
// somar 3 numeros inteiros
// somar 4 numeros inteiros
//somar 2 numeros inteiros e 2 numeros double

//criar uma classe Main capaz de testar todos esses métodos

public class Calculadora {
    private int num1;
    private int num2;
    private int num3;
    private int num4;
    private double num5;
    private double num6;
    private String num7;
    private String num8;

    public int getNum1() {
        return num1;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public int getNum2() {
        return num2;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public int getNum3() {
        return num3;
    }

    public void setNum3(int num3) {
        this.num3 = num3;
    }

    public int getNum4() {
        return num4;
    }

    public void setNum4(int num4) {
        this.num4 = num4;
    }

    public double getNum5() {
        return num5;
    }

    public void setNum5(double num5) {
        this.num5 = num5;
    }

    public double getNum6() {
        return num6;
    }

    public void setNum6(double num6) {
        this.num6 = num6;
    }

    public String getNum7() {
        return num7;
    }

    public void setNum7(String num7) {
        this.num7 = num7;
    }

    public String getNum8() {
        return num8;
    }

    public void setNum8(String num8) {
        this.num8 = num8;
    }


    public int somar(int num1, int num2) {
        return num1 + num2;
    }

    public double somar(double num5, double num6) {
        return num5 + num6;
    }

    // fazer a conversão de tipo e somar dois numeros string
    public String somar(String num7, String num8) {
        int num7int = Integer.parseInt(num7);
        int num8int = Integer.parseInt(num8);
        return String.valueOf(num7int + num8int);
    }

    public int somar(int num1, int num2, int num3) {
        return num1 + num2 + num3;
    }

    // somar dois inteiros e dois double
    public double somar(int num1, int num2, double num5, double num6) {
        return num1 + num2 + num5 + num6;
    }
}








