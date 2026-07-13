class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        int longest = 0;

        for (int num: set) {
            int currNum = 0;
            int currLen = 0;
            if (!set.contains(num - 1)) {
                currLen++;
                currNum = num;

                while (set.contains(currNum+1)) {
                    currLen++;
                    currNum++;
                }
            }
            longest = Math.max(longest, currLen);
        }
        return longest;
    }
}
