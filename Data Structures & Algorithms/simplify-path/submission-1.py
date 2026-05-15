class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []

        for s in path_list:
            if not s or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        return "/" + "/".join(stack)