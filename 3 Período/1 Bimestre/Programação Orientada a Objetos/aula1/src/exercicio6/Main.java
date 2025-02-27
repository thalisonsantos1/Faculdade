package exercicio6;

public class Main {
    public static void main(String[] args) {
        Conta c = new Conta();
        c.saque(10);
        System.out.println(c.saldo);
        c.deposito(100);
        System.out.println(c.saldo);
        c.alteraLimite(200);
        System.out.println(c.limite);
        c.saque(350);
        c.aumentaLimite(100);        
        System.out.println("Seu novo limite é: " + c.verificaLimite());
        c.diminuiLimite(50);
        System.out.println("Seu novo limite é: " + c.verificaLimite());
        System.out.println("Seu saldo é de: " + c.saldo);
        c.saque(340);
        System.out.println("Seu saldo é de: " + c.saldo);
        c.saque(1);
    }
}
