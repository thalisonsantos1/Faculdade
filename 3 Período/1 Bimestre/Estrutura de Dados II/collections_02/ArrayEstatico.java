public class ArrayEstatico {
    public static void main(String[] args) {
        Produto[] produtos = new Produto[3]; //criar um array de 3 posições
        produtos[0] = new Produto(" ", -100.0); //adicionar um produto na primeira posição
        produtos[1] = new Produto("Mouse", 70); //adicionar um produto na segunda posição
        produtos[2] = new Produto("teclado", 90); //adicionar um produto na terceira posição

        System.out.println("ELEMENTOS DO VETOR");

        for (Produto p : produtos) {
            System.out.println(p);
        }
    }
}
