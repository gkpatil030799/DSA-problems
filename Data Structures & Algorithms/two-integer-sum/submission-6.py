class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap = {}
        for index,num in enumerate(nums):
            if num not in countmap:
                countmap[num]= [index]
            else:
                countmap[num].append(index)

        for num in nums:
            x = target - num
            if x in countmap and x!=num:
                return countmap[num]+countmap[x]
            elif x==num and len(countmap[num]) >= 2:
                return [countmap[num][0],countmap[num][1]]
        
        