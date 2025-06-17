package exercicio2;

public class RadioRelogio implements Relogio, Radio {

    @Override
    public void ajustarHorario() {
       System.out.println("Ajustar Horario"); 
    }

    @Override
    public void mostrarHorario() {
        System.out.println("Mostrar Horario");
    }

    @Override
    public void mudarEstacao() {
        System.out.println("Mudar Estacao");
    }

    @Override
    public void aumentarVolume() {
        System.out.println("Aumentar Volume");
    }

    @Override
    public void diminuirVolume() {
        System.out.println("Diminuir Volume");
    }

}
