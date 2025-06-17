package classesabstratas.exemplo1;

public abstract class Veiculo {
    private String modelo;
    private String marca;
    private double valorDoVeiculo;
    private double impostoVeiculo;


    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getValorDoVeiculo() {
        return valorDoVeiculo;
    }
    public void setValorDoVeiculo(double valorDoVeiculo) {
        this.valorDoVeiculo = valorDoVeiculo;
    }

    public double getImpostoVeiculo() {
        return impostoVeiculo;
    }
    public void setImpostoVeiculo(double impostoVeiculo) {
        impostoVeiculo = valorDoVeiculo * impostoVeiculo;
    }

    public abstract String getNomeImposto ();
    public abstract double getValorImposto(double valorDoVeiculo);
  
}
