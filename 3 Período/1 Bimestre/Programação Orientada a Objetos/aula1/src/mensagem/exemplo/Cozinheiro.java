
public class Cozinheiro {
    public String nome;
    

    public Cozinheiro() {}

    public Cozinheiro(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void cozinhar(String prato) {
        System.out.println("Adiciona ingredientes");
        System.out.println("Coloca no fogo");
        System.out.println("Adiciona temperos");
        System.out.println("Monta o prato");

        if (prato.equals ("macarrão")) {
            System.out.println("Faz o molho");
        } else if (prato.equals ("risoto")) {
            System.out.println("Prepara o caldo de legumes");
        } else if (prato.equals ("pizza")) {
            System.out.println("Aquece o forno");
            System.out.println("Faz a massa");
        } else if (prato.equals ("tapioca")) {
            System.out.println("Adiciona o recheio na tapioca");
        }

    }
    
}
