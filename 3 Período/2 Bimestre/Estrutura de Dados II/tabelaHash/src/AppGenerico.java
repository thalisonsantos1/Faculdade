public class AppGenerico {
private static HashTableGenerico<String, Funcionario> tabela = new HashTableGenerico<>();
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario("123", "Joaquim");
        tabela.cadastrar(f1.getDocumento(), f1);

        System.out.println(tabela);
    }
}
