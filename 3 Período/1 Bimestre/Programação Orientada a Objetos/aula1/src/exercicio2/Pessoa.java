package exercicio2;

//neste exercicio vamos criar uma classe pessoa

public class Pessoa { //classe

    String nome; //atributos
    Double peso; //atributos
    Double altura; //atributos
    
    void alteraNome(String novoNome){ //metodos
        nome = novoNome;
    }

    /*alterar o código dos métodos alteraPeso e alteraAltura
    para que aceite apenas alturas de 0.3 até 3.0 e que o peso seja de 0.1 ate 300.
    Estes permitidos devem ser impressos para o usuario que o valor nao é aceito.
    condições E = &&
    condições ou = || */

    void alteraPeso(double novoPeso){ //metodos
        if (novoPeso < 0.1 && novoPeso > 300){
            System.out.println("Peso nao aceito");
                
        } else {
            peso = novoPeso;       
        }
        
    }
    void alteraAltura(double novaAltura){ //metodos
        if (novaAltura < 0.3 && novaAltura > 3.0){
            System.out.println("Altura nao aceita");
            
        } else {
            altura = novaAltura;            
        }
    }
    String retornaNome(){ //metodos
        return nome;
    }
    double retornaPeso(){ //metodos
        return peso;
    }
    double retornaAltura(){ //metodos
        return altura;
    }
    double retoraImc(){ //metodos
        return peso / (altura * altura);
    }
    
}
    
  
