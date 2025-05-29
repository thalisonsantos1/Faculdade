package interfaces.exemplos;

public class ContaCorrente implements Conta{
    private double saldo;
    private double limite = limitePadrao;

    @Override
    public void mostrarSaldo() {
        System.out.println("Saldo da Conta Corrente: " + saldo);        
    }

    @Override
    public void depositar(double valor) {
        saldo += valor;
    }

    @Override
    public void sacar(double valor) {
        if (valor <= (saldo + limite)) {
            saldo -= valor;
        }else{
            System.out.println("Saldo insuficiente para saque.");
        }
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    
}
