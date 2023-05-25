// leetcode problem #136

class singlenumber {
    public int singleNumber(int[] nums) {
      int tmpCount = 0;

			for(int i = 0; i < nums.length; ++i) {
				tmpCount = 0;
				for (int x = 0; x < nums.length; ++x){
					if(nums[i] == nums[x]){
						tmpCount++;
					}
				}
				if (tmpCount == 1){
					return nums[i];
				}
			}
			return 0;
    }
}