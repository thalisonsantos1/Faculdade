
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class AppArrayList {
    public static void main(String[] args) {
        //array heterogeneo --> armazena valores de diferentes tipos
        ArrayList vetor = new ArrayList();

        vetor.add(231);
        vetor.add("Teste");

        System.out.println(vetor.size());
        System.out.println(vetor);

        //armazenar apenas numeros inteiros
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(3214);
        //nums.add("TEste"); // erro de tipo de dado

        Random random = new Random();            

        for (int index = 0; index < 10; index++) {
            nums.add(random.nextInt(1000));
            System.out.println(nums);
        }

        boolean estaNoArray = nums.contains(8);
        System.out.println(estaNoArray);
        //função para ordenar os elementos de uma Array List
        Collections.sort(nums);
        System.out.println(nums);

    }

}
