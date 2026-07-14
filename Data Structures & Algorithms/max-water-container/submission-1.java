class Solution {
    public int maxArea(int[] heights) {
        int currArea = 0;
        int maxArea = 0;
        int l=0;
        int r=heights.length-1;

        while (l<r) {
            currArea = (r-l) * Math.min(heights[l], heights[r]);
            maxArea = Math.max(currArea, maxArea);

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
}
