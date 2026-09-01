class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    #    count = Counter(tasks)
    #    maxHeap = [-cnt for cnt in count.values()] 
    #    heapq.heapify(maxHeap)
    #    time = 0
    #    q = deque()

    #     while maxHeap or q:
    #         time+=1

    #         if maxHeap:
    #             cnt = 1+heapq.heappop(maxHeap)
    #             if cnt:
    #                 q.append([cnt, time+n])
    #         if q and q[0][1] == time:
    #             heapq.heappush(maxHeap, q.popleft()[0])
    #     return time

        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0

        while maxheap or q:
            time+=1
            if maxheap:
                x=1+heapq.heappop(maxheap)
                if x:
                    q.append([x,time+n])
            
            if q and time==q[0][1]:
                heapq.heappush(maxheap, q.popleft()[0])
        return time 
            


















