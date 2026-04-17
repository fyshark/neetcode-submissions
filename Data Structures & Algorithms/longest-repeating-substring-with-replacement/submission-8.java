class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, max = 0, res = 0;
        int[] arr = new int[26];

        for (int r = 0; r < s.length(); r++) {
            arr[s.charAt(r) - 'A']++;
            System.out.println(Arrays.toString(arr));

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
