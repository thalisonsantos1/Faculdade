import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.FileWriter;
import java.io.FileReader;
import java.util.ArrayList;


public class GerenciadorJson {
    private static Gson gson = new Gson();

    public static boolean salvar(ArrayList<String> nomes, String arquivo) {
        try (FileWriter writer = new FileWriter(arquivo)) {
            gson.toJson(nomes, writer);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
    
    public static ArrayList<String> carregar(String arquivo) {
        try (FileReader reader = new FileReader(arquivo)) {
            return gson.fromJson(reader, new TypeToken<ArrayList<String>>() {}.getType());
        } catch (Exception e) {
            return null;
        }
    }


}