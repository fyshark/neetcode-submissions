class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();

        for (char ch: s.toCharArray()) {
            if (ch != ']') {
                stack.push(String.valueOf(ch));
            } else {
                String curr = "";
                while (!stack.peek().equals("[")) {
                    curr = stack.pop() + curr;
                }
                stack.pop();

                String num = "";
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    num = stack.pop() + num;
                }
                int repeat = Integer.parseInt(num);
                StringBuilder sb = new StringBuilder();
                for (int i=0; i<repeat; i++) {
                    sb.append(curr);
                }
                stack.push(sb.toString());
            }
        }
        StringBuilder ans = new StringBuilder();
        for (String str: stack) {
            ans.append(str);
        }
        return ans.toString();
    }
}