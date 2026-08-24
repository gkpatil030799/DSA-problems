class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map = {}
        # for num in nums:
        #     if num in map:
        #         map[num]+=1
        #     else:
        #         map[num]=1

        # valx =  sorted(list(map.values()))
        # lastk = valx[-k:]
        # # result = [key for key,val in map.items() if val in lastk] 
        # # return result   

        # res=[]
        # for key, val in map.items():
        #     if val in lastk:
        #         res.append(key) 
        # return res

        map = {}
        for val in nums:
            if val in map:
                map[val]+=1
            else:
                map[val]=1

        valx = sorted(list(map.values()))
        lastk = valx[-k:]
        result = [ key for key, val in map.items() if val in lastk]
        return result























