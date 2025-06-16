import java.util.TreeMap;

public class AppTs {
    public static void main(String[] args) {
        TreeMap <String, Integer> arvore = new TreeMap();
        arvore.put("ch0", 0);
        arvore.put("ch1", 1);
        arvore.put("ch2", 2);
        arvore.put("ch3", 3);
        arvore.put("ch4", 4);
        arvore.put("ch5", 5);
        arvore.put("ch6", 6);
        arvore.put("ch7", 7);
        arvore.put("ch8", 8);
        arvore.put("ch9", 9);

        System.out.println(arvore);
        System.out.println(arvore.get("ch5"));
    }
}
