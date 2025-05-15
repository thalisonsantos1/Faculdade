public final class Pessoas { // final impede herança por outras classes

    private String nome;
    private double altura;
    private double peso;
    private final double IMCMINIMO = 25; // final impede alteração


    // fazendo sobrecarga de construtores

    public Pessoas(String nome) {
        this.nome = nome;
    }

    public Pessoas (String nome, double altura){
        this.nome = nome;
        this.altura = altura;
    }

    public Pessoas (String nome, double altura, double peso){
        this.nome = nome;
        this.altura = altura;
        this.peso = peso;
    }
    
    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getAltura() {
        return altura;
    }
    public void setAltura(double altura) {
        this.altura = altura;
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public double getIMCMINIMO() {
        return IMCMINIMO;
    }

    // Implementar o método calcularIMC()
    // implementar outro método chamado verificarIMC() que vai calcular o imc e retornar true se a pessoa está com imc <= IMCMINIMO

    public double calcularIMC() {
        return peso / (altura * altura);
    }

    public double calcularIMC(double peso, double altura) {
        this.peso = peso;
        this.altura = altura;
        return peso / (altura * altura);
    }

    public boolean verificarIMC(){
        if (calcularIMC() <= IMCMINIMO) {
            return true;
        } else {
            return false;
        }
    }    

}
