package ava.ava1;

public class Main {
    public static void main(String[] args) {
        SistemaMarketing sistema = new SistemaMarketing("User_marketing", "senha123", "abctoken-syz", 1001);
        System.out.println("Nome do usuário: " + sistema.getNomeUsuario());
        System.out.println("Token: " + sistema.getToken());
        System.out.println("Código do colaborador: " + sistema.getCodigoColaborador());
    }

}
