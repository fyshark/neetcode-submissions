class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory = path.split('/')

        for c in directory:
            if not c or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)