class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        final_amt = 0
        while l<r:
            x = min(heights[l],heights[r])
            y = r-l
            amt = x*y
            final_amt = max(final_amt,amt)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return final_amt

        