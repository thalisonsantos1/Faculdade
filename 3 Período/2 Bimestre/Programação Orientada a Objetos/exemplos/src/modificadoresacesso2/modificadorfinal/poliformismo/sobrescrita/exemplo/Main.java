package exemplo;

import java.util.LinkedList;



public class Main {
    public static void main(String[] args) {

        LinkedList<Pessoa> lista = new LinkedList<>();

        Pessoa p = new Pessoa();
        p.setNome("Bill");
        //p.agradecer();
        lista.add(p);

        Homem h = new Homem();
        h.setNome("Bob");
        //h.agradecer();
        lista.add(h);

        Mulher m = new Mulher();
        m.setNome("Sue");
        //m.agradecer();
        lista.add(m);
        
        for (Pessoa p1 : lista) {
            p1.agradecer();
        }
    }
}
