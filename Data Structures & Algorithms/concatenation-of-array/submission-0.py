class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l=len(nums)
        ans = [0] * (2 * l)

        for n in range(l):
            ans[n] = nums[n]
            ans[n+l] = nums[n]
        return ans 
       
        


        