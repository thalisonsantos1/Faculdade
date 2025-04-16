public class Aluno {

    private String nome;
    private String telefone;
    private double nota1;
    private double nota2;
    private int faltas;
    private Curso curso;

    public Aluno() {

    }

    public Aluno(String nome) {
        this.nome = nome;        
    }

    public Aluno(String nome, String telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public double getNota1() {
        return nota1;
    }

    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }

    public double getNota2() {
        return nota2;
    }

    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }

    public int getFaltas() {
        return faltas;
    }

    public void setFaltas(int faltas) {
        this.faltas = faltas;
    }

    public Curso getCurso() {
        return curso;
    }

    public void setCurso(Curso curso) {
        this.curso = curso;
    }

    public double getMedia() {
        return (nota1 + nota2) / 2;
    }

    public boolean estaAprovado() {
        return getMedia() >= 70 && faltas < 20;
    }

}