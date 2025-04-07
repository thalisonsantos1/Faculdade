    import java.util.Vector;

    public class AppVectorLIst {
        public static void main (String []args){
        Vector<Produto> listaArray = new Vector<Produto>();
        Produto arroz = new Produto("Arroz", 32.5);
        listaArray.add(arroz);
        listaArray.add(new Produto("Feijao", 25.5));
        listaArray.add(new Produto("Macarrao", 15.5));
        
        System.out.println("Vector de Produtos: ");
        for (Produto p : listaArray) {
            System.out.println(p);
        }

    }


}
