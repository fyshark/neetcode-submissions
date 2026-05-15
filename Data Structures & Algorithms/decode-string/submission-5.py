class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr = ''
                while stack and stack[-1] != '[':
                    curr += stack.pop()
                curr = curr[::-1]
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = num[::-1]
                stack.extend(curr * int(num))
        
        return "".join(stack)