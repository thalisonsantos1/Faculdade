public class Produto {
    private String nome;
    private double preco;

    // construtor
    public Produto(String nome, double preco) {
        setNome(nome);
        setPreco(preco); 
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome.isBlank()){
            nome = "Produto padrão";
        }
        
        this.nome = nome.toUpperCase();
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        if (preco < 0.0){
            preco *= -1;
        }
        this.preco = preco;
    }

    @Override
    public String toString() {
        return "Produto: " + getNome() + ", Preço: R$ " + getPreco();
    }

    
}
