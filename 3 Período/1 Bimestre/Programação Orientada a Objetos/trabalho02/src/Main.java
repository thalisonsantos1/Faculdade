import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // cadastrando um curso
        System.out.println("--- CADASTRO DO CURSO ---");
        System.out.println("Digite o nome do curso: ");
        String nomeCurso = sc.nextLine();
        Curso curso = new Curso(nomeCurso);

        // cadastrando um professor
        System.out.println("--- CADASTRO DO PROFESSOR ---");
        System.out.println("Digite o nome do professor: ");
        String nomeProfessor = sc.nextLine();
        Professor professor = new Professor(nomeProfessor);
        curso.setProfessor(professor);

    }
    
}
