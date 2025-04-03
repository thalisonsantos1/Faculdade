/* Desenvolva uma aplicação em java, utilizando os conceitos de POO, para cadastro e controle de clientes e seus pedidos, onde:
 - um pode ter zero, um ou muitos pedidos;
 - um pedido é de um único cliente.

 
 */

public class Clientes {
    private String nome;
    private String telefone;
    private Pedidos pedidos;

    public Clientes(String nome, String telefone) {
        setNome(nome);
        setTelefone(telefone);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public Pedidos getPedidos() {
        
        return pedidos;
    }

    public void setPedidos(Pedidos pedidos) {
        this.pedidos = pedidos;
    }

    public void addPedido(Pedidos p) {
        this.pedidos = p;
    }


    
}
