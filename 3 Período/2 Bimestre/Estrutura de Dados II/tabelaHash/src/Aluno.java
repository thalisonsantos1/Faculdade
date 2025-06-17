public class Aluno {
    private String matricula;
    private String nome;
    private String curso;
    private String email;

    public Aluno(String matricula, String nome, String curso, String email) {
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.email = email;
    }

    @Override
    public String toString() {
        return "Aluno{" +
                "matricula='" + matricula + '\'' +
                ", nome='" + nome + '\'' +
                ", curso='" + curso + '\'' +
                ", email='" + email + '\'' +
                '}';
    }

    

}
