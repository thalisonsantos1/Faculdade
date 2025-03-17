public class VetorDeObjetos {
    public static void imprimir(double []v){
        for (int i = 0; i < v.length; i++) {
            System.out.print(v[i]);
        }
    }

    public static void imprimir(Object []aux){
        for (int i = 0; i < aux.length; i++) {
        System.out.print(aux[i] + "");
    }
            
        }
        /*public static void imprimir(String []aux){
            for (int i = 0; i < aux.length; i++) {
                System.out.print(aux[i] + "");
                
            }
        }

        public static void imprimir(Conta []aux){
            for (int i = 0; i < aux.length; i++) {
                System.out.print(aux[i] + "");
                
            }
    }*/


    public static void main(String[] args) {
        double []v = new double[4]; // [0.0, 0.0, 0.0, 0.0]
        imprimir(v);
        String []palavras = new String[4]; // [null, null, null, null]
        //imprimir(palavras);
        Conta []minhasContas = new Conta[3]; // [null, null, null]
        imprimir(minhasContas);
        Double []w = new Double[4]; // [null, null, null, null]
        imprimir(w);
    }
    
}
