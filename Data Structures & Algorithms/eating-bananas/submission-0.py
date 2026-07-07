class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def pode(k):
            # quantas horas o macaco comeria a pilha dado esse rating k?
            horas = 0
            for bananas in piles:
                resto = bananas % k  
                horas += (bananas//k)
                if resto != 0:
                    horas += 1
                
            if horas <= h:
                return True
            else:
                return False
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if pode(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

