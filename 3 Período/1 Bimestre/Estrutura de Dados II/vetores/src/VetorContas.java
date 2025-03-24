public class VetorContas {
    public static void main(String[] args) {
        
    

    // vetor estático --> vantagem: acesso a posição do vetor ser mais rápido, por ser estático
    // desvantagem: se precisarmos alocar mais posições
    // vetor de int -> [4, 2, 3, 8, 10, 6]
    // Conta -> [c1, c2, c3, c4, c5]
    // preciso armazernar mais 6 elementos
    
    int [] vetor = new int [5];
    vetor[0] = 4;
    vetor[1] = 2;
    vetor[2] = 8;
    vetor[3] = 10;
    vetor[4] = 6;

    // novo vetor com mais 6 elementos
    int [] vetor2 = new int [vetor.length + 6];
    vetor2[0] = vetor[0];
    vetor2[1] = vetor[1];
    vetor2[2] = vetor[2];
    vetor2[3] = vetor[3];
    vetor2[4] = vetor[4];
    // alternativa
    for (int i = 0; i < vetor.length; i++) {
        vetor2[i] = vetor[i];
    }
    
    
    }

}
