/*Crie uma classe Pessoa, com os atributos nome, telefone e email. Crie ainda um atributo estático (da classe) chamado Contador.
 * A cada objeto Pessoa instanciado, incremente automaticamente um número na variável Contador.
 * Instancie 10 pessoas e mostre no final, o valor da variável contador.
 */

package modificadoresacesso2.estatico.exercicio;

public class Pessoa {
    private String nome;
    private String telefone;
    private String email;
    private static int contador = 0;
    
    
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public static int getContador() {
        return contador;
    }

    public static void setContador(int contador) {
        Pessoa.contador = contador;
    }

    public Pessoa() {        
        contador++;
    }
}
