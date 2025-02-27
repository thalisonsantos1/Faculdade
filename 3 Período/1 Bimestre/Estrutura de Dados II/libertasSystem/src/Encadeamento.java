import java.util.Scanner;

public class Encadeamento {

    public static void main (String[]args) {
        int x = 2;
        Scanner in = new Scanner(System.in);

        System.out.println("Digite um valor: ");
        int y = in.nextInt();
        switch (y) {
            case 1:
                System.out.println("Escolhi 1");
                break;
            case 2:
                System.out.println("escolhi 2");
                break;
            case 3:
                System.out.println("escolhi 3");
                break;
            default:
                System.out.println("caso padrão");
                break;
        }
    }

}
