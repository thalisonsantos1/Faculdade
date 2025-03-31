import java.util.ArrayList;
import java.util.List;

public class Responsavel {
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
    private Endereco endereco;
    private List<Crianca> criancas = new ArrayList<>();

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }   

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public List<Crianca> getCriancas() {
        return criancas;
    }

    public void addCrianca(Crianca criancas) {
        this.criancas.add(criancas);
    }
}
