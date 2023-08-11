import java.util.*;

public class test {
    public static void main(String[] args){
        List<String> words = new ArrayList<>();

        words.add("one.two.three");
        words.add("four.five");
        words.add("six");

        splitWordsBySeparator(words, '.');
    }

    public static List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> res = new ArrayList<>();
        for(int i = 0; i < words.size(); i++){
            String [] split = words.get(0).split(separator + "");
            
            for(int x = 0; x < split.length; x++){
                System.out.println(split[x]);
                System.out.println("im gay");
                res.add(split[x]);
            }
        }
        
        return res;
    }
}
