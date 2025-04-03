public class Garcom {

    
        public String nome;
        private Cozinheiro cozinheiro;
        public String nomeDoPrato;


        public Garcom(String nome) {
            this.nome = nome;
        }

        public String getNome() {
            return nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        
        public Cozinheiro getCozinheiro() {
            return cozinheiro;  
        }

        public void setCozinheiro(Cozinheiro cozinheiro) {
            this.cozinheiro = cozinheiro;
        }

        public void atender() {
            System.out.println("Atendendo o cliente");
            
            
        }

        public void atender(String prato) {
            System.out.println("Anota o pedido");
            cozinheiro.cozinhar(prato);
            System.out.println("Entrega o prato");
        } 

}
