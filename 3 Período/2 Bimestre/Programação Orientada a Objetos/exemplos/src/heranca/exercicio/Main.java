package heranca.exercicio;

public class Main {
    public static void main(String[] args) {
        
        Motorista motorista = new Motorista();
        motorista.setNome("Thalison");
        motorista.setCategoria("A");
        motorista.setCpf("123456789");
        motorista.setIdade(50);
        motorista.setNumeroCnh("123456789");
        motorista.aniversario();
    

        Moto m = new Moto();
        m.setCapacete("Capacete");
        m.setModelo("Honda CBX750");
        m.setAno(2020);
        m.setMarca("Honda");
        m.setPlaca("ABC1234");
        m.setMotorista(motorista);
        

        Carro c = new Carro();
        c.setCapPortaMalas(400);
        c.setModelo("Honda");
        c.setAno(2020);
        c.setMarca("Honda Civic");
        c.setPlaca("ABC4321");
        c.setMotorista(motorista);
        
    }
}
