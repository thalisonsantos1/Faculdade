package ava.ava1;

public class SistemaMarketing implements LoginPortal{
    private String nomeUsuario;
    private String senha;
    private String token;
    private int codigoColaborador;

    public SistemaMarketing(String nomeUsuario, String senha, String token, int codigoColaborador) {
        this.nomeUsuario = nomeUsuario;
        this.senha = senha;
        this.token = token;
        this.codigoColaborador = codigoColaborador;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }


    public String getSenha() {
        return senha;
    }


    public String getToken() {
        return token;
    }

    public int getCodigoColaborador() {
        return codigoColaborador;
    }

}
