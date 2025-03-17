package exercicio3;

public class veiculo { //classe

    String  modelo;
    String  marca;
    String  placa;
    int     anoFabricacao;
    double  valor;
    
public veiculo(){
    System.out.println("construindo o objeto Veiculo");
    anoFabricacao = 2000;

}


    int IdadeCarro(){
//       Date time = new date(now);
        //int anoAtual = 2025;
        return 2025 - anoFabricacao;
    }

    double ValorIPVA(){
        int AnoMinimo = 1970;
        if (anoFabricacao > AnoMinimo){
            return 0.04 * valor;
        } else {
            return 0;
        }
    }

    double valorSeguro(){
        return 0.06 * valor;
    }
}   
