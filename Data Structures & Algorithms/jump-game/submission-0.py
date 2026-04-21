class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-2
        goal = len(nums)-1
        while i >= 0:
            t = nums[i]
            if i+t >= goal:
                goal=i
            i-=1
        if goal > nums[0]:
            return False
        else:
            return True
                
            