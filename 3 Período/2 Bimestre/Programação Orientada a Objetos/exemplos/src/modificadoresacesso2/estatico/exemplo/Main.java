package modificadoresacesso2.estatico.exemplo;

public class Main {
    public static void main(String[] args) {

        Produto p1 = new Produto();
        p1.setDescricao("iPhone 11 Pro Max");
        p1.setPreco(1000.0);
        Produto.setCotacaoDolar(5.66);

        Produto p2 = new Produto();
        p2.setDescricao("Macbook");
        p2.setPreco(1500.0);
        Produto.setCotacaoDolar(5.99);

        System.out.println(p1.getDescricao() + ": " + p1.getPrecoReal());
        System.out.println(p2.getDescricao() + ": " + p2.getPrecoReal());
        
    }
}
