class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) {
            return new String();
        }

        int[] map = new int[128];
        int start = 0, end = 0, startIndex = 0, minLen = Integer.MAX_VALUE;

        for (char ch: t.toCharArray()) {
            map[ch]++;
        }
        char[] chS = s.toCharArray();
        int count = t.length();

        while (end < chS.length) {
            if (map[chS[end]] > 0) {
                count--;
            }
            map[chS[end]]--;
            end++;

            while (count == 0) {
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }

                if (map[chS[start]] == 0) {
                    count++;
                }
                map[chS[start]]++;
                start++;
            }
        }
        return minLen == Integer.MAX_VALUE ? new String() :
            new String(chS, startIndex, minLen);

    }
}
