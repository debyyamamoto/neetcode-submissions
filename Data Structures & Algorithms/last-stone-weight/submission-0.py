class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = []
        for i in stones:
            neg_stones.append(-i)
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            stone1 = heapq.heappop(neg_stones)
            heapq.heapify(neg_stones)
            stone2 = heapq.heappop(neg_stones)
    
            if (stone1 == stone2):
                continue
            else:
                if stone1 < stone2:
                    son = stone2 - stone1
                else:
                    son = stone1 - stone2

                heapq.heappush(neg_stones, -son)
        if len(neg_stones) == 0:
            return 0
        else:
            return -(neg_stones[0])