package classesabstratas.exemplo1;

public class Barco extends Veiculo {
    private int numeroRegistro;

    public String getNomeImposto(){
        return "IMPOSTO PORTUÁRIO";
    }

    public int getNumerRegistro() {
        return numeroRegistro;
    }

    public void setNumerRegistro(int numerRegistro) {
        this.numeroRegistro = numeroRegistro;
    }

    public double getValorImposto(double valorDoVeiculo) {
        return valorDoVeiculo * 0.08;
    }

}
