package modificadoresacesso.pacote1;

public class Pessoa {
    // atributos privados: são associados apenas dentro da própria classe
    private String nome;
    private int idade;

    // construtor de ser sempre publico
    //acessivel por qualquer classe

    public Pessoa (String novoNome, int novaIdade) {
        nome = novoNome;

        if (novaIdade >= 0 && novaIdade <= 120){
            idade = novaIdade;
        }else {
            idade = 0;
            System.out.println("Idade inválida");
        }
        /*if (idade >= 0 && idade <= 120) {
            idade = novaIdade;            
        }else {
            idade = 0;
            System.out.println("Idade inválida");
        }*/
        
    }
    
    //atributo publico: acesível por qualquer classe
    public String pegaNome () {
        return nome;
    }
    public int pegaIdade () {
        return idade;
    }
    //atributo protegido: acessível por outras classes
    //apenas do mesmo pacote
    protected void aniversario () {
        idade++;
    }

    public void alteraIdade (int novaIdade) {
        if (novaIdade >= 0 && novaIdade <= 120) {
            idade = novaIdade;            
        }else {
            idade = 0;
            System.out.println("Idade inválida");
        }
    }




    /*public void alteraIdade (int novaIdade) {
        if (idade >= 0 && idade <= 120) {
            idade = novaIdade;            
        }else {
            idade = 0;
            System.out.println("Idade inválida");
        }
    }*/

    
}
