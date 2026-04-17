class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, maxLen = 0, res = 0;

        char[] arr = new char[26];
        for (int r = 0; r < s.length(); r++) {
            arr[s.charAt(r) - 'A']++;
            maxLen = Math.max(maxLen, arr[s.charAt(r) - 'A']);

            if (r - l + 1 - maxLen > k) {
                arr[s.charAt(l) - 'A']--;
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
