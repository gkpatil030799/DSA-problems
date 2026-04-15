class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num]=1
            else:
                map[num]+=1
        
        valx = sorted(list(map.values()) ) 
        lastk = valx[-k:]
        result = [key for key, value in map.items() if value in lastk]
        return result
    
    
                