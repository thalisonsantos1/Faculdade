public class App {
    public static void imprimir(int []aux){
        for (int i = 0; i < aux.length; i++) {
            System.out.println(i + " >> " + aux[i]);
        }
    }

    public static void imprimir(String []aux){
        for (int i = 0; i < aux.length; i++) {
            System.out.println(i + " >> " + aux[i]);
        }
    }

    public static void main(String[] args) {
       int tamanho = 15;
       int []numeros = new int[tamanho];
       System.out.println(numeros);
       String []palavras = {"ola", "mundo", "teste"};
       System.out.println(palavras);
       //Cliente []clientes = new Cliente[100];
       //System.out.println(clientes);

       // adicionando elementos no vetor numeros
       numeros[5] = 357;
       imprimir(numeros);
       imprimir(palavras);
    }
}
