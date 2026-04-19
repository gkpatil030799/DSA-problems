class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i:i[0])
        prevend = intervals[0][1]
        count = 0
        res = []
        for i in range(1,len(intervals)):
            if intervals[i][0] < prevend:
                prevend = min(prevend,intervals[i][1])
                count+=1
            else:
                prevend = intervals[i][1]
                res.append(intervals[i])
        return count
