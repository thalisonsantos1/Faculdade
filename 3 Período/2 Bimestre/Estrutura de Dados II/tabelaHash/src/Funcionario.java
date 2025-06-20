import br.com.caelum.stella.bean.vadation.logic.*;

public class Funcionario {
    private String documento;
    private String nome;
    private double salario;
    private CPF validador = new CPFV();

    public Funcionario(String documento, String nome) {
        setDocumento(documento);
        setNome(nome);
        
    }

    public String getDocumento() {
        return documento;
    }

    private void setDocumento(String documento) {
        this.documento = documento;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome.toUpperCase();
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }




    @Override
    public String toString() {
        return "Documento: " + getDocumento() + "\t Nome: " + getNome() + "\t Salario: R$ " + getSalario();
    }

    


}
