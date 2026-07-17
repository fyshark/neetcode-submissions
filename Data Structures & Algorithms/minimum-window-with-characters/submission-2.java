class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) {
            return new String();
        }

        int start = 0, end = 0, minLen = Integer.MAX_VALUE, count = t.length();
        int startIndex = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (char ch: t.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        char[] chS = s.toCharArray();

        while (end < s.length()) {
            char cr = chS[end];
            if (map.containsKey(chS[end])) {
                if (map.get(cr) > 0) {
                    count--;
                }
                map.put(cr, map.get(cr)-1);
            }
            end++;

            while (count == 0) {
                char cl = chS[start];
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }

                if (map.containsKey(cl)) {
                    map.put(cl, map.get(cl)+1);   
                    if (map.get(cl) > 0) {
                        count++;
                    }
                }
                start++;
            }
        }
        return minLen == Integer.MAX_VALUE ? new String() : new String(chS, startIndex, minLen);
    }
}
