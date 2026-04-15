class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i:i[0])
        lst = [intervals[0]]
        for R in range(1, len(intervals)):
            if intervals[R][0] <= lst[-1][1] :
                lst[-1][1] = max(lst[-1][1],intervals[R][1])

            else:
                lst.append(intervals[R])

        return lst