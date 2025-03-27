package associacao.exemplo;

public class Main {
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario();
        f1.setNome("Bill Gates");

        Funcionario f2 = new Funcionario();
        f2.setNome("Steve Jobs");

        Funcionario f3 = new Funcionario();
        f3.setNome("Maria");

        Funcionario f4 = new Funcionario();
        f4.setNome("Severino");

        Departamento d = new Departamento();
        d.setNome("Departamento de TI");

        Departamento d2 = new Departamento();
        d2.setNome("Recepcao");
        
        // fazendo a associacao entre funcionarios e departamento

        f1.setDepartamento(d);
        d.getFuncionarios().add(f1);

        f2.setDepartamento(d);
        d.getFuncionarios().add(f2);

        //imprimindo funcionario:

        System.out.println(f1.getNome() + " trabalha no departamento " + f1.getDepartamento().getNome());

        //imprimindo departamento:

        System.out.println(d.getNome() + " possui " );
        for (Funcionario f : d.getFuncionarios()) {
            System.out.println(f.getNome());
        }

        //adicione a funcionária Maria ao departamento de TI:

        

        //adicione o Severino que trabalha na Recepção


    }
}
