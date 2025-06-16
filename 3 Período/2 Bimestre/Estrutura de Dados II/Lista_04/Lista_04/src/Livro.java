public class Livro implements Comparable<Livro> {
    private String titulo;
    private int ano;

    public Livro(String titulo, int ano) {
        this.titulo = titulo;
        this.ano = ano;
    }

    public String getTitulo() {
        return titulo;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String toString() {
        return "Livro{" +
                "titulo='" + titulo + '\'' +
                ", ano=" + ano +
                '}';
    }

    @Override
    public int compareTo(Livro outro) {
        return this.ano - outro.ano;
    }


}
