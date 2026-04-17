class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0)+1
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pair of [-cnt, idleTime]
        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time