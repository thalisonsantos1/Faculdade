
import java.util.ArrayList;
import java.util.Collections;

public class AppArrayListMetodos {
    public static void main(String[] args) {
        ArrayList<String> palavras = new ArrayList<String>(); // criando um arraylist de strings
        palavras.add("casa");
        palavras.add("chuva");
        palavras.add("arara");
        palavras.add(1, "mouse"); // adicionando um elemento na posicao 1
        System.out.println(palavras);

        // consulta o elemento na posicao 1
        String palavra = palavras.get(3);
        System.out.println("Palavra na posicao 3: " + palavra);

        // recuperando a ultima palavra da estrutura
        System.out.println("Palavra na ultima posicao: " + palavras.getLast());

        // recuperando a primeira palavra da estrutura
        System.out.println("Palavra na primeira posicao: " + palavras.getFirst());

        // ordenar o arraylist
        Collections.sort(palavras);
        System.out.println("ordenada" + palavras);

        // verificar a quantidade de elementos
        System.out.println("Quantidade de elementos: " + palavras.size());

        // remover um elemento da estrutura
        String el = palavras.remove(2);
        System.out.println("Elemento removido: " + el);
        System.out.println(palavras);
        System.out.println("Retirar mouse: " + palavras.remove("mouse"));
        System.out.println("Retirar tv: " + palavras.remove("tv"));
        System.out.println(palavras);

        // testando a inserção de elemento duplicado
        palavras.add("arara");
        System.out.println(palavras);
        
        //adicionando elemento somente se ele nao existir na estrutura
        /*if (!palavras.contains("arara"))
            palavras.add("arara");*/

        palavras.add("arara");
        System.out.println(palavras);

    

    }

}
