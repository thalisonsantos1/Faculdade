package modificadoresacesso2.estatico.exercicio;

public class Main {
    public static void main(String[] args) {
        
        Pessoa p1 = new Pessoa();
        p1.setNome("Thalison");
        p1.setTelefone("35991662015");
        p1.setEmail("fulano@oi.com.br");
        
        Pessoa p2 = new Pessoa();
        p2.setNome("Fulano");
        p2.setTelefone("35991662016");
        p2.setEmail("fulano@oi.com.br");
        
        Pessoa p3 = new Pessoa();
        p3.setNome("Ciclano");
        p3.setTelefone("35991662017");
        p3.setEmail("fulano@oi.com.br");

        Pessoa p4 = new Pessoa();
        p4.setNome("Beltrano");
        p4.setTelefone("35991662018");
        p4.setEmail("fulano@oi.com.br");
        
        
        Pessoa p5 = new Pessoa();
        p5.setNome("Beltrano");
        p5.setTelefone("35991662018");
        p5.setEmail("fulano@oi.com.br");
        
        Pessoa p6 = new Pessoa();
        p6.setNome("Beltrano");
        p6.setTelefone("35991662018");
        p6.setEmail("fulano@oi.com.br");
        
        Pessoa p7 = new Pessoa();
        p7.setNome("Beltrano");
        p7.setTelefone("35991662018");
        p7.setEmail("fulano@oi.com.br");
        
        Pessoa p8 = new Pessoa();
        p8.setNome("Beltrano");
        p8.setTelefone("35991662018");
        p8.setEmail("fulano@oi.com.br");

        Pessoa p9 = new Pessoa();
        p9.setNome("Beltrano");
        p9.setTelefone("35991662018");
        p9.setEmail("fulano@oi.com.br");
        
        Pessoa p10 = new Pessoa();
        p10.setNome("Beltrano");
        p10.setTelefone("35991662018");
        p10.setEmail("fulano@oi.com.br");
        
        System.out.println("Foram instanciadas " + Pessoa.getContador() + " pessoas");
        
        
        
    }
         
}
