public class Tipos {
    public static void main(String[] args) {
        System.out.println(Byte.MAX_VALUE);
        System.out.println(Byte.MIN_VALUE);
        byte numero = 127;
        System.out.println("----teste----");
        System.out.println(numero);
        //numero = ++numero;
        System.out.println(++numero);
        //System.out.println(++numero);

        ///tipos primitos inteiros

        byte    valor2 = -128; 
        byte    valor1 = 127; // byte -> 7 bits para o número e 1 bit para o sinal
        short   valor3 = 32767; // short -> 15 bits para o número e 1 bit para o sinal
        short   valor4 = -32768;
        int     valor5 = 2147483647; // int -> 31 bits para o número e 1 bit para o sinal
        //int     valor6 = -2147483648;
        //long    valor7 = 9223372036854775807L; // long -> 63 bits para o número e 1 bit para o sinal
        //long    valor8 = -9223372036854775808L;
        float   valor6 = 1.0f/3.0f;
        double  valor7 = 1.0/3.0;
        
    System.out.println("----teste----");
    System.out.println(valor6);
    System.out.println(valor7);

    //caracteres
    char valor8 = 'a';
    char valor9 = 'A';

    System.out.println(valor8);
    System.out.println(valor9);

    valor8++; //valor8 + 1
    // valor9 = valor9 + 1; dá erro
    System.out.println(valor8);
    char valor10 = 100;
    System.out.println(valor10);
    int valor11 = '$';
    System.out.println(valor11);

    /*caracteres especiais
     \n - enter (quebra de linha)
     \t - tabulacao
     \f - formfeed (quebra de pagina)
     \' - para exibir o apostrofo */
     System.out.println("\fola mundo\nhoje\testa\" calor");
    // string assim está errado. String assim ok
    //string não é primitivo, ela é uma classe
    String valor12 = "O que é, o que é?";
    System.out.println(valor12);
    System.out.println(valor12.toUpperCase());
    System.out.println(valor12.length());

    //tipo lógico - boolean
    boolean valor13 = true;
    boolean valor14 = false;
    System.out.println(valor13);
    System.out.println(valor14);

   



        

    }
}
