import java.util.ArrayList;
import java.util.List;

public class Curso {
    private String nome;
    private Professor professor;
    private List<Aluno> alunos = new ArrayList<>();

    public Curso (String nome){
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void addAluno(Aluno aluno){
        alunos.add(aluno);        
    }

    public Professor getProfessor() {
        return professor;
    }

    public void setProfessor(Professor professor) {        
        this.professor = professor;
    }

    public List<Aluno> getAlunos() {
        return alunos;
    }
}
