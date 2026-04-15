class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for val in nums:
            if val in map:
                map[val]+=1
            else:
                map[val]=1

        for i,val in map.items():
            if val > 1:
                return True
        return False
            