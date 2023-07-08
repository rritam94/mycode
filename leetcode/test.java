import java.util.*;

public class test {
    public static void main(String[] args){
        int [] nums = {1,6,7,8};
        int moveFrom [] = {1,7,2};
        int moveTo [] = {2,9,5};

        System.out.println(occupiedPositions(nums,moveFrom,moveTo));
    }

    public static List<Integer> occupiedPositions(int[] nums, int[] moveFrom, int[] moveTo) {
        Set<Integer> positions = new HashSet<>();
        
        for (int num : nums) {
            positions.add(num);
        }
        
        for (int i = 0; i < moveFrom.length; i++) {
            int from = moveFrom[i];
            int to = moveTo[i];
            
            positions.remove(from);
            positions.add(to);
        }
        
        List<Integer> result = new ArrayList<>(positions);
        Collections.sort(result);
        
        return result;
    }
}
