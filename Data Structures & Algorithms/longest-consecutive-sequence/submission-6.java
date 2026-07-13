class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }
        int n = nums.length;
        int longest = 0;

        for (int num: set) {
            if (!set.contains(num - 1)) {
                int currentLen = 1;
                int currentNum = num;

                while (set.contains(currentNum+1)) {
                    currentLen++;
                    currentNum++;
                }
                longest = Math.max(longest, currentLen);
            }
        }
        return longest;
    }
}
