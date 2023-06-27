import java.util.HashMap;
import java.util.Map;

class Solution {
    public static boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();

        for(int i = 0; i < ransomNote.length(); i++){
            if(!map.containsKey(ransomNote.charAt(i))){
                map.put(ransomNote.charAt(i), 1);
            }
            else {
                map.put(ransomNote.charAt(i), map.get(ransomNote.charAt(i)) + 1);
            }
        }

        for(int i = 0; i < magazine.length(); i++){
            if(!map.containsKey(magazine.charAt(i))){
                map.put(magazine.charAt(i), 1);
            }
            else {
                map.put(magazine.charAt(i), map.get(magazine.charAt(i)) - 1);
            }
        }

        return map.size() == 0;
    }

    public static void main(String [] args){
        System.out.println(canConstruct("bruh", "bruh"));
    }
}