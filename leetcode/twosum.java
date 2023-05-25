// leetcode problem #1!

class twosum {
    public int[] twoSum(int[] nums, int target) {
        int [] array = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int x = i + 1; x < nums.length; x++){
                if(nums[i] + nums[x] == target){
                    array[0] = i;
                    array[1] = x;
                    return array;
                }
            }
        }
        return null;
    }
}
