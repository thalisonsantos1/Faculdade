import java.util.ArrayList;
import java.util.List;

public class Crianca {
    private String nome;
    private int idade;
    private List<Responsavel> responsavels = new ArrayList<>();

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public List<Responsavel> getResponsavels() {
        return responsavels;    
    }

    public void addResponsavel(Responsavel responsavel) {
        this.responsavels.add(responsavel);
    }
}
