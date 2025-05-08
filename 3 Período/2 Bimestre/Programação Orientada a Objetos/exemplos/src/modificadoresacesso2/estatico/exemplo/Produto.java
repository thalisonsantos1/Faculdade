package modificadoresacesso2.estatico.exemplo;

public class Produto {
    private String descricao;
    private double preco;
    private static double cotacaoDolar;

    
    
    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public static double getCotacaoDolar() {
        return cotacaoDolar;
    }
    public static void setCotacaoDolar(double cotacaoDolar) {
        Produto.cotacaoDolar = cotacaoDolar;
    }

    public double getPrecoReal(){
        return cotacaoDolar * preco;
    }
}
