class Solution {
    public int search(int[] nums, int target) {
        int l = 0, n = nums.length - 1;
        
        while(l <= n) {
            int m = l + ((n - l)/2);
            if (target < nums[m]) {
                n = m - 1;
            } else if (target > nums[m]) {
                l = m + 1;
            } else {
                return m;
            }
        }
        return -1;
    }
}
