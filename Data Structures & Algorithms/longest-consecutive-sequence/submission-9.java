class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int longest = 1;
        int n = nums.length;
        int currentLen = 1;

        if (nums.length == 0) {
            return 0;
        }

        for (int i=1; i<n; i++) {
            if (nums[i] == nums[i-1]) {
                continue;
            }
            if (nums[i] == nums[i-1] + 1) {
                currentLen++;
            } else {
                currentLen = 1;
            }
            
            longest = Math.max(longest, currentLen);
            
        }
        return longest;
    }
}
