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

        // cadastrando alunos
        System.out.println("--- CADASTRO DOS ALUNOS ---");
        String continuar = "S";

        while (continuar.equalsIgnoreCase("S")) {
            System.out.println("Digite o nome do aluno: ");
            String nomeAluno = sc.nextLine();

            System.out.println("Digite o telefone do aluno: ");
            String telefoneAluno = sc.nextLine();

            
            Aluno aluno = new Aluno(nomeAluno, telefoneAluno);
            
            System.out.println("Nota 1 (0 a 100): ");
            aluno.setNota1(Double.parseDouble(sc.nextLine()));

            System.out.println("Nota 2 (0 a 100): ");
            aluno.setNota2(Double.parseDouble(sc.nextLine()));

            System.out.println("Informe a quantidade de faltas: ");
            aluno.setFaltas(Integer.parseInt(sc.nextLine()));

            curso.addAluno(aluno);

            System.out.println("Deseja inserir mais alunos no curso? (S/N): ");
            continuar = sc.nextLine();
        }

        // Resultados

        System.out.println("--- RESULTADOS FINAIS ---");
        System.out.println("Nome do curso: " + curso.getNome());
        System.out.println("Professor: " + professor.getNome());
        System.out.println("Alunos: ");

        for (Aluno aluno : curso.getAlunos()) {
            double media  = aluno.getMedia();
            String status = aluno.estaAprovado() ? "Aprovado" : "Reprovado";
            System.out.println("Nome: " + aluno.getNome());
            System.out.println("Média: " + media);
            System.out.println("Faltas: " + aluno.getFaltas());
            System.out.println("Status: " + status);
            System.out.println("------------------");
        }
            
    }
    
}
