import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class topk {
    public static void main(String [] args){
        topKFrequent(new int [] {1,1,1,2,2,3}, 2);
    }

    public static void topKFrequent(int[] nums, int k) {
        int ret [] = new int[k];
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int curr = nums[i];
            if(!map.containsKey(curr)){
                map.put(curr, 1);
            }

            else{
                map.put(curr, map.get(curr) + 1);
            }
        }

        for(int i = 0; i < k; i++){
            int currKey = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
            ret[i] = currKey;
            map.remove(currKey);
        }

        // return ret;
    }
}
