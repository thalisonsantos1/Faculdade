import java.util.ArrayList;
import java.util.Collections;

public class GerenciadorNomes {
    private ArrayList<String> nomes;

        public GerenciadorNomes() {
            this.nomes = new ArrayList<>();
        }

        //método para adiciocar nomes se for válido
        public boolean adicionaNome(String nome){
            if (nome == null || nome.trim().isEmpty()){
                System.out.println("Erro: nome não pode ser vazio!!");
                return false;
            }
            if (nomes.contains(nome)){
                System.out.println("Erro: o nome informado já existe na Lista!!");
                return false;
            }
            nomes.add(nome);
            return true;
        }


        // método para realizar a remoção de um nome existente
        public boolean removeNome(String nome){
            return nomes.remove(nome);
        }

        // buscando um nome existente na lista
        public boolean buscaNome(String nome){
            return nomes.contains(nome);
        }

        // Retornando a lista ordenada
        public ArrayList<String> nomesOrdenados(){
            Collections.sort(nomes);
            return nomes;
        }

        public ArrayList<String> getNomes(){
            return nomes;
        }

        public void setNomes(ArrayList<String>nomes){
            if (nomes != null) {
                this.nomes = nomes;
            } else {
                this.nomes = new ArrayList<>();
            }
        }   
        
}
    

