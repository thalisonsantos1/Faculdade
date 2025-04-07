import java.util.ArrayList;

public class AppArrayList {
    public static void main(String[] args) {
        ArrayList<Produto> listaArray = new ArrayList<Produto>();
        Produto arroz = new Produto("Arroz", 32.5);
        listaArray.add(arroz);
        listaArray.add(new Produto("Feijao", 25.5));
        listaArray.add(new Produto("Macarrao", 15.5));
        
        System.out.println("ArrayList de Produtos: ");
        for (Produto p : listaArray) {
            System.out.println(p);
        }

    }    
}
// reproduza esta classe usanto linkedlist e vector