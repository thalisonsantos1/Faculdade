package model;

import java.util.Objects;


public class Rota {
    private Cidade destino;
    private int distancia;

    public Rota(Cidade destino, int distancia) {
        this.destino = destino;
        this.distancia = distancia;
    }

    public Cidade getDestino() {
        return destino;
    }

    public int getDistancia() {
        return distancia;
    }

    @Override
    public String toString(){
        return "Destino: " + destino.getNome() + ", Distancia: " + distancia + "km";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Rota)) return false;
        Rota rota = (Rota) o;
        return Objects.equals(destino, rota.destino);
    }

    @Override
    public int hashCode() {
        return Objects.hash(destino);
    }
}
