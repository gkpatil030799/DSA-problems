class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i,k,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            if i > n:
                return
            
            #decision to include
            comb.append(i)
            backtrack(i+1,k,comb)
            comb.pop()

            #decision to exclude
            backtrack(i+1,k,comb)
        backtrack(1,k,[])
        return res