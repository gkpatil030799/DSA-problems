class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0]*3
        for num in nums:
            counts[num]+=1
        n = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[n] = i
                n+=1

        return nums        