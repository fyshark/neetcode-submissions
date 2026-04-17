class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, n = numbers.length - 1;

        while(l < n) {
            int curSum = numbers[l] + numbers[n];
            if(curSum > target) {
                n--;
            } else if(curSum < target) {
                l++;
            } else {
                return new int[] {l + 1, n + 1};
            }
        }
        return new int[0];
    }
}
