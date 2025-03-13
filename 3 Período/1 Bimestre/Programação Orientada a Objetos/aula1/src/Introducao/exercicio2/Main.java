package exercicio2;

// neste exercicio vamos aplicar a classe pessoa criada anteriormente
public class Main {

    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        pessoa.alteraNome("João Silva");
        pessoa.alteraAltura(1.65);
        pessoa.alteraPeso(70.0);

        System.out.println("Nome:   " + pessoa.retornaNome());
        System.out.println("Altura: " + pessoa.retornaAltura());
        System.out.println("Peso:   " + pessoa.retornaPeso());
        System.out.println("IMC:    " + pessoa.retoraImc());
        
    }
    
}
