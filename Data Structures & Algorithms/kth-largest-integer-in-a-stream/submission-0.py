class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        heap = []
        heapq.heappush(heap,val)
        for i in self.nums:
            heapq.heappush(heap, i)
            if len(heap) > self.k:
                heapq.heappop(heap)
        self.nums = heap
        return heap[0]