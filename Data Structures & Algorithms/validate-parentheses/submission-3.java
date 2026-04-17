class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        Map<Character, Character> bracketsLookup = new HashMap<>(3);

        bracketsLookup.put(']', '[');
        bracketsLookup.put('}', '{');
        bracketsLookup.put(')', '(');

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(bracketsLookup.containsKey(c)) {
                if(!brackets.isEmpty() && bracketsLookup.get(c).equals(brackets.peek())) {
                    brackets.pop();
                } else {
                    return false;
                }
            } else {
                brackets.push(c);
            }
        }
        return brackets.isEmpty();
    }
}
