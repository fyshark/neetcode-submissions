class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, right = 0;
        int maxProfit = 0;

        while(right < prices.length) {
            if (prices[left] > prices[right]) {
                left = right;
            } else {
                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            }
            right++;
        }
        return maxProfit;
    }
}
