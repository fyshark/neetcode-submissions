class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = steps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far+1):
                farthest = max(farthest, nums[i] + i)
            
            near = far+1
            far = farthest
            steps += 1
        
        return steps