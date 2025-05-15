public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        calc.setNum1(10);
        calc.setNum2(20);
        calc.setNum3(30);
        calc.setNum4(40);
        calc.setNum5(50.0);
        calc.setNum6(60.0);
        calc.setNum7("70");
        calc.setNum8("80");

        System.out.println("Soma 2 inteiros: " + calc.somar(10, 20));
        System.out.println("Soma 2 doubles: " + calc.somar(50.0, 60.0));
        System.out.println("Soma 2 strings: " + calc.somar("70", "80"));
        System.out.println("Soma 3 inteiros: " + calc.somar(10, 20, 30));
        System.out.println("Soma 4 inteiros: " + calc.somar(10, 20, 30, 40));
        System.out.println("Soma 2 inteiros e 2 doubles: " + calc.somar(10, 20, 50.0, 60.0));
    }
}
