class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0 and stack[-1] < -a:
                stack.pop()

            if stack and stack[-1] > 0 and a < 0 and stack[-1] > -a:
                continue

            if stack and stack[-1] > 0 and a < 0 and stack[-1] == -a:
                stack.pop()
                continue
            
            stack.append(a)
        
        return stack