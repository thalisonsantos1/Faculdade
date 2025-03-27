package associacao.exemplo;

public class Funcionario {
    private String nome;
    private Departamento departamento; // primeiro classe e depois objeto

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Departamento getDepartamento() {
        return departamento;
    }    

    public void setDepartamento(Departamento dep) {
        this.departamento = dep;
    }
}
