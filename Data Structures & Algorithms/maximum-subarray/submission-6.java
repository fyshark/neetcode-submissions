class Solution {
    public int maxSubArray(int[] nums) {
        return divide(nums, 0, nums.length-1);
    }

    private int divide(int[] nums, int left, int right) {
        if (left == right) return nums[left];
        int mid = (left + right)/2;
        int leftMax = divide(nums, left, mid);
        int rightMax = divide(nums, mid+1, right);

        int sum = 0;
        int leftSum = Integer.MIN_VALUE;
        for (int i=mid; i>=left; i--) {
            sum += nums[i];
            leftSum = Math.max(leftSum, sum);
        }

        sum = 0;
        int rightSum = Integer.MIN_VALUE;
        for (int i=mid+1; i<=right; i++) {
            sum += nums[i];
            rightSum = Math.max(sum, rightSum);
        }
        int crossSum = leftSum + rightSum;
        return Math.max(crossSum, Math.max(leftMax, rightMax));
    }
}
