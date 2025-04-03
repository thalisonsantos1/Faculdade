

public class Pedidos {
    private String produto;
    private int quantidade;
    private double preco;

    public Pedidos(String produto, int quantidade, double preco) {
        setProduto(produto);
        setQuantidade(quantidade);
        setPreco(preco);
        
    }

    public String getProduto() {
        return produto;
    }

    public void setProduto(String produto) {
        this.produto = produto;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }


    

    
}
