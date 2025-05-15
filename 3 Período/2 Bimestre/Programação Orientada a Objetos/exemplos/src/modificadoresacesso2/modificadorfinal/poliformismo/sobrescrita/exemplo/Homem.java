import exemplo.Pessoa;

//package sobrescrita.exemplo;
public class Homem extends Pessoa{

    @Override
    public void agradecer() {
        System.out.println("Muito obrigado");
    }

}
