package exercicio3;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
  
        Veiculo veiculo = new Veiculo();
        Scanner in = new Scanner(System.in);        
           
    
    System.out.println("Informe o modelo do veículo: ");
    veiculo.modelo = in.nextLine();

    System.out.println("Informe a marca do veículo: ");
    veiculo.marca = in.nextLine();

    System.out.println("Informe a placa do veiculo: ");
    veiculo.placa = in.nextLine();

    System.out.println("Informe o ano de fabricação do veículo: ");
    veiculo.anoFabricacao = in.nextInt();

    System.out.println("Informe o valor do veículo: ");
    veiculo.valor = in.nextDouble();
    
    
    
    DecimalFormat df=new DecimalFormat("###,##0.00");
    System.out.println("Modelo: " + veiculo.modelo);
    System.out.println("Marca: "  + veiculo.marca);
    System.out.println("Placa: "  + veiculo.placa);
    System.out.println("Ano: "    + veiculo.anoFabricacao);
    System.out.println("Valor: "  + df.format (veiculo.valor));
    System.out.println("IPVA: "   + df.format (veiculo.ValorIPVA()));
    System.out.println("Seguro: " + df.format (veiculo.valorSeguro()));
    System.out.println("Idade: "  + veiculo.IdadeCarro() + " anos");

    }
}

