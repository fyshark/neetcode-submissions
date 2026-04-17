class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder cleanedString = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                cleanedString.append(Character.toLowerCase(c));
            }
        }

        int n = cleanedString.length();
        for (int i = 0; i < (n/2); i++) {
            if (cleanedString.charAt(i) != cleanedString.charAt(n - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
