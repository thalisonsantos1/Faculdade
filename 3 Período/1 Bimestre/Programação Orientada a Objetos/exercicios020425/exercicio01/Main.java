
// Cliente Donald fez 2 pedidos e Patinhas fez 3 pedidos

public class Main {
    public static void main(String[] args) {
        Clientes c1 = new Clientes("Donald", "123456789");
        Clientes c2 = new Clientes("Patinhas", "987566987");

        Pedidos p1 = new Pedidos("camisa", 100, 50.0);
        Pedidos p2 = new Pedidos("calcado", 200, 25);
        Pedidos p3 = new Pedidos("calcado", 300, 35.6);
        Pedidos p4 = new Pedidos("calcado", 400, 40);
        Pedidos p5 = new Pedidos("calcado", 500, 45);

        

        c1.addPedido(p1);
        c1.addPedido(p2);

        c2.addPedido(p3);
        c2.addPedido(p4);
        c2.addPedido(p5);


        System.out.println("o cliente " +c1.getNome() + " fez " + c1.getPedidos() + " pedidos.");
        System.out.println("o cliente " +c2.getNome() + " fez " + c2.getPedidos() + " pedidos.");
    }

    



}
