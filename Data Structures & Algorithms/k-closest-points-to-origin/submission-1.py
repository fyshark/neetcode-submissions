class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance = -(point[0]**2 + point[1]**2)
            max_heap.append((distance, point[0], point[1]))
        heapq.heapify(max_heap)

        while len(max_heap) > k:
            _, x, y = heapq.heappop(max_heap)
        
        return [[x, y] for _, x, y in max_heap]