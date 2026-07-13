class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        int longest = 0;
        int n = nums.length;
        for (int num: set) {
            if (!set.contains(num-1)) {
                int currentNum = num;
                int currentLength = 1;
                while (set.contains(currentNum+1)) {
                    currentLength++;
                    currentNum++;
                }
                longest = Math.max(longest, currentLength);
            }
            
        }
        return longest;
    }
}
