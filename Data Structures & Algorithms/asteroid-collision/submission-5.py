class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while stack and stack[-1] > 0 and a < 0:

                if stack[-1] < -a:
                    stack.pop()

                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive == True:
                stack.append(a)

        return stack