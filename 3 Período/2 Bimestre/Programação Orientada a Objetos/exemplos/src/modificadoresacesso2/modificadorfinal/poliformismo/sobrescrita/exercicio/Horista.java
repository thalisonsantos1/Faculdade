// Crie uma classe horista que herda da classe funcionario e tem o atributo horastrabalhadas. 
// Faça sobrescrita do método getSalarioTotal de maneira que o calculo do seu salario de acordo com as horas trabalhadas, sendo que o valor do salario é com base em 160 horas mensais e deve-se calcular o salario proporcional para depois somar com o vale alimentação.


package exercicio;

public class Horista extends Funcionario{
    private double horasTrabalhadas;

    public double getHorasTrabalhadas() {
        return horasTrabalhadas;
    }

    public void setHorasTrabalhadas(double horasTrabalhadas) {
        this.horasTrabalhadas = horasTrabalhadas;
    }

    @Override
    public double getSalarioTotal() {
        return ((super.getSalario()/160)*horasTrabalhadas) + super.getValeAlimentacao();
        
    }



    

}
