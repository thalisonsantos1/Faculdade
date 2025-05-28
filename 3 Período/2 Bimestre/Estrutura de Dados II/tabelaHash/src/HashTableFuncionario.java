
import java.util.Hashtable;
import java.util.Scanner;

public class HashTableFuncionario {
    private static Scanner input = new Scanner(System.in);
    private static Hashtable <String, Funcionario> funcs = new Hashtable <>(); // aqui voce define a chave e o valor ()
    
    public static int menu(){
        System.out.println("1 -Cadastrar");
        System.out.println("2- Listar todos");
        System.out.println("3- Buscar pelo CPF");
        System.out.println("0 - Sair");
        System.out.println("Escolha: ");
        int op = input.nextInt(); //limpar buffer
        input.nextLine();
        return op;
    }
    public static void cadastrar() {
        System.out.println("---Cadastro---");
        System.out.println("CPF: ");
        String cpf = input.nextLine();
        if (funcs.contains(cpf)){
            System.out.println("CPF ja cadastrado!");
            System.out.println("....vamos de novo...");
            cadastrar();
        }else{
            System.out.println("Nome: ");
            String nome = input.nextLine();
            System.out.print("Salario: ");
            double salario = input.nextDouble();
            Funcionario obj = new Funcionario(cpf, nome);
            obj.setSalario(salario);
            funcs.put(cpf, obj);
            System.out.println("Funcionario cadastrado com sucesso!");
        }
        
    }
    
    public static Funcionario buscar(){
        System.out.println("---Busca---");
        System.out.print("CPF: ");
        String cpf = input.nextLine();    
        if (funcs.containsKey(cpf)){
            Funcionario f = funcs.get(cpf);
            System.out.println(f);
            return f;
        }
        System.out.println("CPF " + cpf + " nao encontrada!");
        return null;

    }
 
    public static void main(String[] args) {
        int opcao = 0;
        do{
            opcao = menu();
            switch(opcao){
                case 1:
                    cadastrar();
                    break;
                case 2:
                    System.out.println("---Listagem---");
                    if (funcs.isEmpty()){
                        System.out.println("Nenhum aluno cadastrado!");
                    }else{
                        for (String cpf : funcs.keySet()){
                            Funcionario f = funcs.get(cpf);
                            System.out.println(f);
                        }
                    }
                    break;
                case 3:
                    buscar();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;//
                default:
                System.out.println("Opção inválida!");
            }
        }while(opcao!=0);
        
    }
}
