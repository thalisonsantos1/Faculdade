
import java.util.ArrayList;
import java.util.List;

public class Cidade {
    private String nome;
    private String estado;
    private List<Endereco> enderecos = new ArrayList<>();

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEstado() {
        return estado;    
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public List<Endereco> getEnderecos() {
        return enderecos;
    }

    public void addEnderecos(Endereco endereco) {
        this.enderecos.add(endereco);
    }

}
