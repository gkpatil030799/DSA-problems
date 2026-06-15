class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  prevMap = {}

        #  for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     else:
        #         prevMap[n] = i

        map = {}

        for i,val in enumerate(nums):
            diff = target-val
            if diff in map:
                return [map[diff],i]
            else:
                map[val] = i

            

        