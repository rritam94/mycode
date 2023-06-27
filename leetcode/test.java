import java.util.*;

public class test {
    public static void main(String[] args){
        // System.out.println(maximumNumberOfStringPairs(new String [] {"cd","ac","dc","ca","zz"}));
        System.out.println();
    }

    public static int[] maxSlidingWindow(int[] nums, int k) {
       int left = 0;
       int right = k - 1;
       int max = Integer.MIN_VALUE;
       List<Integer> l = new ArrayList<>();
       boolean check = false;

        while(right < nums.length){
            if(!check){
                for(int i = left; i <= right; i++){
                    max = Math.max(max, nums[i]);
                }
                check = true;
                l.add(max);
            }

            else {
                System.out.println(left - 1);
                if(max != nums[left - 1]){
                    max = Math.max(nums[right], max);
                }
                else{
                    for(int i = left; i <= right; i++){
                        max = Math.max(max, nums[i]);
                    }
                }
                l.add(max);
            }

            left++; right++;
        }
        
        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}
