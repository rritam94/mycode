import java.util.HashMap;
import java.util.Map;
public class groupanagrams {
    public static void main(String[] args) {
        Map<Character [], Integer> map = new HashMap<>();
    }

    static int ascii(String s){
        int sum = 0;
        for(int x = 0; x < s.length(); x++){
            sum += (int) (s.charAt(x));
        }
        return sum; 
    }
}
