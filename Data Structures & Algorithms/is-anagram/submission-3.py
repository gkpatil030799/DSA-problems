class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0)
        #     countT[t[i]] = 1 + countT.get(t[i],0)

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for val in s:
            if val in countS:
                countS[val]+=1
            else:
                countS[val]=1

        for val in t:
            if val in countT:
                countT[val]+=1
            else:
                countT[val]=1

        return countS == countT
