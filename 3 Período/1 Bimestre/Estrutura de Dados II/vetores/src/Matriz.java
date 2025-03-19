public class Matriz {
    public static void main(String[] args) {
        int [][] matriz = new int[5][6];
        //preencher a matriz
        //00 01 02 03 04 05
        //10 11 12 13 14 15
        //20 21 22 23 24 25
        //30 31 32 33 34 35
        //40 41 42 43 44 45
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print("" + i + j + " ");
                matriz[i][j] = i * j;
            }
            System.out.println();            
        }        
        //visualizar a matriz
        for (int[] linha : matriz) {
            for (int elemento : linha) {
                System.out.print(elemento + "\t");
            }
            System.out.println();                 
        }

        System.out.println("linhas " + matriz.length);
        System.out.println("colunas " + matriz[3].length);
        for (int lin = 0; lin < matriz.length; lin++) {
            for (int col = 0; col < matriz[lin].length; col++) {
                int elem = matriz[lin][col];
                System.out.print(elem + "\t");
            }
            System.out.println();
            
        }


        // faça o equivalente usando fori
        /*for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();            
        }*/
    }
}
