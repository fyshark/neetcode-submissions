class Solution {
    public boolean canJump(int[] nums) {
        int max_i = 0;
        for (int i=0; i<nums.length; i++) {
            if (max_i < i) return false;

            int curr_i = nums[i] + i;
            max_i = Math.max(max_i, curr_i);
        }
        return max_i >= nums.length-1;
    }
}
