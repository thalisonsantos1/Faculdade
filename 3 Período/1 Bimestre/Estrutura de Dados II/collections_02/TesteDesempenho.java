import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Random;
import java.util.Vector;

public class TesteDesempenho {
    public static void main(String[] args) {
        int tamanho = 1000000;
        int consulta = 100000;

        int [] array = new int [tamanho];
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        LinkedList<Integer> linkedList = new LinkedList<Integer>();
        Vector<Integer> vectorList = new Vector<Integer>();
        Random aleatorio = new Random();

        for (int i = 0; i < tamanho; i++) {
            array[i] = i;
            arrayList.add(i);
            linkedList.add(i);
            vectorList.add(i);            
        }


        // array estatico
        long inicio = System.currentTimeMillis();
        for (int i = 0; i < consulta; i++) {
            int valor = array[aleatorio.nextInt(tamanho)];
        }
        

        long fim = System.currentTimeMillis();
        //System.out.println("Tempo Array estático: " + (fim - inicio) + "ms");

        

        

        //ArrayList
        inicio = System.currentTimeMillis();        
        for (int i = 0; i < consulta; i++) {
            int valor = arrayList.get(aleatorio.nextInt(tamanho));
        }
        fim = System.currentTimeMillis();
        System.out.println("Tempo ArrayList: " + (fim - inicio) + "ms");    
        
        //LinkedList

        inicio = System.currentTimeMillis();
        

            for (int i = 0; i < consulta; i++) {
                int valor = linkedList.get(aleatorio.nextInt(tamanho));
            }
        
            fim = System.currentTimeMillis();
        System.out.println("Tempo LinkedList: " + (fim - inicio) + "ms");

        //vectorList

        inicio = System.currentTimeMillis();  
        
        for (int i = 0; i < consulta; i++) {
            int valor = vectorList.get(aleatorio.nextInt(tamanho));
        }
        fim = System.currentTimeMillis();
        System.out.println("Tempo Vector: " + (fim - inicio) + "ms");
    
    }
}


