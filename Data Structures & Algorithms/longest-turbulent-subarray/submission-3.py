class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # L = 0
        # diff = 0
        # for R in range(len(arr)-1):
        #     if arr[R] == arr[R+1]:
        #         L=R

        #     else:
        #         maxL, maxR = L,R
        #         diff = max(diff, maxR-maxL+1)
        # return diff

        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r+=1
                prev = ">"

            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r+=1
                prev = "<"

            else:
                if arr[r] == arr[r-1]:
                    r+=1
                else:
                    r=r
                l=r-1
                prev = "="
        return res