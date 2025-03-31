public class Endereco {
    private String logradouro;
    private String numero;
    private String bairro;
    private Responsavel responsavel;
    private Cidade cidade;

    public String getLogradouro() {
        return logradouro;
    }    

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public Responsavel getResponsavel() {
        return responsavel;
    }

    public void setResponsavel(Responsavel responsavel) {
        this.responsavel = responsavel;
    }

    public Cidade getCidade() {
        return cidade;
    }    

    public void setCidade(Cidade cidade) {    
        this.cidade = cidade;
    }
    
}
