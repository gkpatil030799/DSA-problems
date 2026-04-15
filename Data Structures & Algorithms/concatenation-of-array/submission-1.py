class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = []
        # l=len(nums)
        # ans = [0] * (2 * l)

        # for n in range(l):
        #     ans[n] = nums[n]
        #     ans[n+l] = nums[n]
        # return ans 

        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans 
         
       
        


        