package exercicio6;

public class Conta {

    String titular = "João Silva";
    int numeroConta = 1234;
    double saldo = 0;
    double limite = 100;

    
    double saque(double valor){
        if ((saldo+limite) < valor){
            System.out.println("Saldo insuficiente");
            return 0;
        }else
            return saldo -= valor;
    }

    double deposito(double valor){
        return saldo += valor;
    }

    double verificaSaldo(){
        return saldo;
    }

    double verificaLimite(){
        return limite;
    }

    double alteraLimite(double novoLimite){
        return limite = novoLimite;
    }

    double aumentaLimite(double valor){
        return limite += valor;
    }

    double diminuiLimite(double valor){
        return limite -= valor;
    }
}