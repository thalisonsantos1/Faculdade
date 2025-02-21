package exercicio3;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
  
        veiculo veiculo = new veiculo();
        Scanner myObj = new Scanner(System.in);        
           
    
    System.out.println("Informe o modelo do veículo: ");
    veiculo.Modelo = myObj.nextLine();
    System.out.println("Informe a marca do veículo: ");
    veiculo.Marca = myObj.nextLine();
    System.out.println("Informe a placa do veiculo: ");
    veiculo.Placa = myObj.nextLine();
    System.out.println("Informe o ano de fabricação do veículo: ");
    veiculo.anoFabricacao = myObj.nextInt();
    System.out.println("Informe o valor do veículo: ");
    veiculo.Valor = myObj.nextDouble();
    
    
    DecimalFormat df=new DecimalFormat("###,##0.00");
    System.out.println("Modelo: " + veiculo.Modelo);
    System.out.println("Marca: "  + veiculo.Marca);
    System.out.println("Placa: "  + veiculo.Placa);
    System.out.println("Ano: "    + veiculo.anoFabricacao);
    System.out.println("Valor: "  + df.format (veiculo.Valor));
    System.out.println("IPVA: "   + df.format (veiculo.ValorIPVA()));
    System.out.println("Seguro: " + df.format (veiculo.valorSeguro()));
    System.out.println("Idade: "  + veiculo.IdadeCarro() + " anos");
    
    }
  
}

public class veiculo { //classe

    String  Modelo;
    String  Marca;
    String  Placa;
    int     anoFabricacao;
    double  Valor;

    int IdadeCarro(){
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
    double valorSeguro(){
        return 0.01 * Valor;
    }
}