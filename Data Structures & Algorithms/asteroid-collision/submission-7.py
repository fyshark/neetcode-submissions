class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            isAlive = True

            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] > -a:
                    isAlive = False
                    break
                elif stack[-1] < -a:
                    stack.pop()
                else:
                    stack.pop()
                    isAlive = False
                    break

            if isAlive == True:
                stack.append(a)

        return stack