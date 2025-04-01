package exerciciosdeep.exercicio1;

public class Pessoa {
    String nome;
    int idade;
    String cpf;

    public void fazerAniversario() {
        idade ++;
    }

    public void validaCpf(){
        if (cpf.length() == 11){
            System.out.println("CPF Válido");
        } else {
            System.out.println("CPF Inválido. O CPF deve conter 11 dígitos");
        }
    }
    

    public void apresentar (){
        System.out.println(nome + " tem " + idade + " Anos");
    }


}
