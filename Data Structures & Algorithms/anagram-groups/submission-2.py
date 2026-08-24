class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map = defaultdict(list)
        # for s in strs:
        #     arr = [0] * 26
        #     for char in s:
        #         arr[ord(char)-ord("a")]+=1
        #     map[tuple(arr)].append(s)
        # return list(map.values())

        # map = defaultdict(list)
        # for string in strs:
        #     arr = [0]*26
        #     for char in string:
        #         arr[ord(char)-ord("a")]+=1
        #     map[tuple(arr)].append(string)
        # return list(map.values())
        

        map = defaultdict(list)
        for string in strs:
            arr = [0]*26
            for char in string:
                arr[ord(char)-ord("a")]+=1
            map[tuple(arr)].append(string)
        return list(map.values())
            