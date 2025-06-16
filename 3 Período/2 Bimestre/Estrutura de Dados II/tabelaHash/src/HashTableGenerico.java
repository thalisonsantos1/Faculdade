
import java.util.Hashtable;
import java.util.Scanner;
import javax.swing.plaf.basic.BasicTabbedPaneUI;

//META: deixar essa classe GENRICA - 

public class HashTableGenerico <K,T> {
    private Scanner input = new Scanner(System.in);
    private Hashtable <K, T> table = new Hashtable <>(); // aqui voce define a chave e o valor ()
    
    
    public void cadastrar(K key, T object){ {
        System.out.println("---Cadastro---");
              
        if (table.contains(key)){
            System.out.println(key + "ja cadastrado!");
            System.out.println("....vamos de novo...");
            this.cadastrar(key, object);
        }else{
            table.put(key, object);
            System.out.println("...cadastrado com sucesso!");
        }
        
    }
}

    
    public T buscar(K key){
        System.out.println("---Busca---");   
        if (table.containsKey(key)){
            T object = table.get(key);
            System.out.println(object);
            return object;
        }
        System.out.println("Chave " + key + " nao encontrada!");
        return null;

    }

    @Override
    public String toString() {
        String saida = "";
        return  table;
    }
 

}
