class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for word in s:
            if word not in map:
                map[word] = 1
            elif word in map:
                map[word]+=1
        for word in t:
            if word in map:
                map[word]-=1
            else:
                return False

        if all(value==0 for value in map.values()):
            return True
        else:
            return False
          
        