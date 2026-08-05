class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i, j in points:
            dist.append([(i,j),-(i**2 + j**2)])
        heap = []
        count = 0
        for p, d in dist:
            heapq.heappush(heap, (d,count, p))
            if len(heap) > k:
                heapq.heappop(heap)
            count += 1
        res = []
        for _, _, p in heap:
            f, s = p
            res.append([f,s])
        return res