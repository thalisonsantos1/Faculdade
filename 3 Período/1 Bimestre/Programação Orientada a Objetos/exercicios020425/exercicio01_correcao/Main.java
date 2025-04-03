public class Main {
    public static void main(String[] args) {
        Cliente c1 = new Cliente();
        c1.setNome("Donald");
        c1.setTelefone("123456789");

        Cliente c2 = new Cliente();
        c2.setNome("Patinhas");
        c2.setTelefone("987566987");

        Pedido p1 = new Pedido();
        p1.setProduto("camisa");
        p1.setQuantidade(100);
        p1.setPreco(50.0);

        // associaçao
        p1.setCliente(c1);
        c1.getPedidos().add(p1);

        Pedido p2 = new Pedido();
        p2.setProduto("calcado");
        p2.setQuantidade(200);
        p2.setPreco(25.0);

        // associaçao
        p2.setCliente(c1);
        c1.getPedidos().add(p2);

        Pedido p3 = new Pedido();
        p3.setProduto("blusa");
        p3.setQuantidade(300);
        p3.setPreco(35.6);


        // associaçao
        p3.setCliente(c2);
        c2.getPedidos().add(p3);

        Pedido p4 = new Pedido();
        p4.setProduto("bone");
        p4.setQuantidade(400);
        p4.setPreco(40.0);

        // associaçao
        p4.setCliente(c2);        
        c2.getPedidos().add(p4);

        Pedido p5 = new Pedido();
        p5.setProduto("calcado");
        p5.setQuantidade(500);
        p5.setPreco(45.0);

        // associaçao
        p5.setCliente(c2);        
        c2.getPedidos().add(p5);

        // exibicao
        System.out.println("Cliente: " +c1.getNome());
        for (Pedido p : c1.getPedidos()) {
            System.out.println("Pedido: " + p.getProduto());
        }
        System.out.println("Cliente: " +c2.getNome());
        for (Pedido p : c2.getPedidos()) {
            System.out.println("Pedido: " + p.getProduto());
        }

    }
}
