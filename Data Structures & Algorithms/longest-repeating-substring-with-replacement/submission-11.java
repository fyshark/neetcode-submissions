class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0, max = 0, l = 0;
        int arr[] = new int[26];

        for (int r = 0; r < s.length(); r++) {
            arr[s.charAt(r) - 'A']++;
            max = Math.max(max, arr[s.charAt(r) - 'A']);

            if (r - l + 1 - max > k) {
                arr[s.charAt(l) - 'A']--;
                l++;
            }
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
