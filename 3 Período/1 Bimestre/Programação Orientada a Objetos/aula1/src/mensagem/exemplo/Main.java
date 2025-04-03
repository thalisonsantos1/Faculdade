public class Main {

    public static void main(String[] args) {
        Cozinheiro c = new Cozinheiro("Erick Jacquin");
        Garcom g = new Garcom("Joaquim");

        // associação do cozinheiro para o garçom

        g.setCozinheiro(c); // garcom recebe o cozinheiro

        //executa a ação com envio de mensagem

        g.atender("pizza"); 
        g.atender("tapioca"); // garcom chama o metodo atender

        // adicione um parametro String na ação do Garçom de atender. Neste parametro deve ser passado o nome do prato. O garçom deve repassar este nome do prato para o cozinheiro.
        // Quando o cozinheiro for cozinhar ele deverá ter os seguintes passos adicionais:
        // Se o prato for macarrão, fazer o molho;
        // Se o prato for risoto, preparar o caldo de legumes;
        // Se o prato for pizza, aquecer o forno e fazer a massa;
        // Se o prato for tapioca, adicionar o recheio na tapioca.

    }
}
