class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for (int i=0; i<n-2; i++) {
            int l = i+1;
            int r = n-1;
            if (i>0 && nums[i]==nums[i-1]) {
                continue;
            }

            while (l<r) {
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum > 0) {
                    r--;
                }else if (threeSum < 0) {
                    l++;
                }else {
                    List<Integer> threeSumList = Arrays.asList(nums[i], nums[l], nums[r]);
                    l++;
                    r--;
                    res.add(threeSumList);
                    while (l<r && nums[l] == nums[l-1]) {
                        l++;
                    }
                    
                }
            }
        }
        return res;
    }
}
