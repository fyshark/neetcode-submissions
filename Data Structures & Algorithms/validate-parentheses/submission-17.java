class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of(
            ']','[', 
            '}','{', 
            ')','('
        );
        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()) {
            if (map.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != map.get(c)) {
                    return false;
                }

            } else {
                stack.push(c);
            }
        }
        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}
