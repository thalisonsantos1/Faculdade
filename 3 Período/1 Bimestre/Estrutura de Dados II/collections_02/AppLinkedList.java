

import java.util.LinkedList;



public class AppLinkedList {
   
    public static void main(String[] args) {
        LinkedList<Produto> listaArray = new LinkedList<Produto>();
        Produto arroz = new Produto("Arroz", 32.5);
        listaArray.add(arroz);
        listaArray.add(new Produto("Feijao", 25.5));
        listaArray.add(new Produto("Macarrao", 15.5));
        
        System.out.println("linkedList de Produtos: ");
        for (Produto p : listaArray) {
            System.out.println(p);
        }

    }
}
