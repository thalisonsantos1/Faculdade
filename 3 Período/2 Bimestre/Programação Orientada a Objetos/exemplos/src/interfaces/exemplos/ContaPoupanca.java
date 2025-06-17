package interfaces.exemplos;

public class ContaPoupanca implements Conta {
    private double saldo;

    @Override
    public void mostrarSaldo() {
        System.out.println("Saldo da Conta Poupança: " + saldo);
    }

    @Override
    public void depositar(double valor) {
        saldo += valor;
    }

    @Override
    public void sacar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente para saque.");
        }
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }


    
}
