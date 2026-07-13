class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;

        while (l < r) {
            char cl = s.charAt(l);
            char cr = s.charAt(r);
            if (!Character.isLetterOrDigit(cl)) {
                l++;
            }
            if (!Character.isLetterOrDigit(cr)) {
                r--;
            }

            if (Character.isLetterOrDigit(cl) && Character.isLetterOrDigit(cr)) {
                if (Character.toLowerCase(cl) == Character.toLowerCase(cr)) {
                    l++;
                    r--;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
