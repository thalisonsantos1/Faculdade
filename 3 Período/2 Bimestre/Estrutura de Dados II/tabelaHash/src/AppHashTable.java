
import java.util.Hashtable;
import java.util.Scanner;

public class AppHashTable {
    private static Scanner input = new Scanner(System.in);
    private static Hashtable <String, String> alunos = new Hashtable <>(); // aqui voce define a chave e o valor ()
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
        alunos.put(matricula, nome);
    }
    public static String buscar(){
        System.out.println("---Busca---");
        System.out.println("Matricula: ");
        String matricula = input.nextLine();    
        

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
                    System.out.println(alunos);
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
