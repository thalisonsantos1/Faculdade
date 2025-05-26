
import java.util.Hashtable;
import java.util.Scanner;

public class AppHashTable {
    private static Scanner input = new Scanner(System.in);
    private static Hashtable <String, Aluno> alunos = new Hashtable <>(); // aqui voce define a chave e o valor ()
    public static int menu(){
        System.out.println("1 -Cadastrar");
        System.out.println("2- Listar todos");
        System.out.println("3- Buscar pela chave");
        System.out.println("0 - Sair");
        System.out.println("Escolha: ");
        int op = input.nextInt(); //limpar buffer
        input.nextLine();
        return op;
    }
    public static void cadastrar() {
        System.out.println("---Cadastro---");
        System.out.println("Matricula: ");
        String matricula = input.nextLine();
        if (alunos.contains(matricula)){
            System.out.println("Matricula ja cadastrada!");
            return; // paro a execução do metodo
        }        
        
        System.out.println("Nome: ");
        String nome = input.nextLine();
       
        
        System.out.println("Curso: ");
        String curso = input.nextLine();
        
        System.out.println("Email: ");
        String email = input.nextLine();
       
        Aluno a = new Aluno(matricula, nome, curso, email);
        alunos.put(matricula, a);

        System.out.println("Aluno cadastrado com sucesso!");
        
        
        
    }
    public static Aluno buscar(){
        System.out.println("---Busca---");
        System.out.println("Matricula: ");
        String matricula = input.nextLine();    
        if (alunos.containsKey(matricula)){
            Aluno a = alunos.get(matricula);
            System.out.println("Aluno encontrado: " + a);
            return a;
        }
        System.out.println("Matricula " + matricula + " nao encontrada!");
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
                    if (alunos.isEmpty()){
                        System.out.println("Nenhum aluno cadastrado!");
                    }else{
                        for (String matricula : alunos.keySet()){
                            Aluno a = alunos.get(matricula);
                            System.out.println(a);
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
