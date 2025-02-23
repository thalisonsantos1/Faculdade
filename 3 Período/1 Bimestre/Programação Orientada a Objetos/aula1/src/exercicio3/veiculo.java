package exercicio3;

public class veiculo { //classe

    String  Modelo;
    String  Marca;
    String  Placa;
    int     anoFabricacao;
    double  Valor;

    int IdadeCarro(){
//        Date time = new date(now);
        //int anoAtual = 2025;
        return 2025 - anoFabricacao;
    }

    double ValorIPVA(){
        int AnoMinimo = 1970;
        if (anoFabricacao > AnoMinimo){
            return 0.04 * Valor;
        } else {
            return 0;
        }
    }
