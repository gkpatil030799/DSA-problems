class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        joined = "".join(ch for ch in lower_s if ch.isalnum())
        l,r = 0,len(joined)-1
        while l<r:
            if joined[l] != joined[r]:
                return False
            l+=1
            r-=1 
        return True
