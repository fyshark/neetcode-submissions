class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] candidates, int start, int remain, List<Integer> temp, List<List<Integer>> res) {
        if (remain < 0) {
            return;
        }

        if (remain == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int i=start; i<candidates.length; i++) {
            temp.add(candidates[i]);
            backtrack(candidates, i, remain - candidates[i], temp, res);
            temp.remove(temp.size()-1);
        }
    }
}
