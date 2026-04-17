class Solution {
    public int characterReplacement(String s, int k) {
        
        int n = s.length(), res = 0;

        for (int l = 0; l < n; l++) {
            int max = 0;
            HashMap<Character, Integer> map = new HashMap<>();
            
            for (int r = l; r < n; r++) {
                map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);
                max = Math.max(max, map.get(s.charAt(r)));

                if (r - l + 1 - max <= k) {
                    res = Math.max(res, r - l + 1);
                }
            }
        }
        return res;
    }
}
