class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                countmap[num]+=1

        for num,val in countmap.items():
            if val > 1:
              return True
        return False